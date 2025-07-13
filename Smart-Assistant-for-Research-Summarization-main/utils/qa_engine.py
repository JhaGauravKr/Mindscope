from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM
from sentence_transformers import SentenceTransformer, util
import torch
import random
import re

qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

semantic_model = SentenceTransformer("all-MiniLM-L6-v2")

gen_tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-base")
gen_model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-base")
gen_qa_pipeline = pipeline("text2text-generation", model=gen_model, tokenizer=gen_tokenizer)

gpt2_model = AutoModelForCausalLM.from_pretrained("gpt2")
gpt2_tokenizer = AutoTokenizer.from_pretrained("gpt2")
text_gen = pipeline(
    "text-generation",
    model=gpt2_model,
    tokenizer=gpt2_tokenizer,
    truncation=True,
    max_new_tokens=256,
    pad_token_id=gpt2_tokenizer.eos_token_id
)

GENERIC_QUESTIONS = [
    "What is the main idea of the document?",
    "What problem is the research trying to solve?",
    "What is the conclusion or result mentioned?"
]

def split_context(context, max_chunk_words=250):
    words = context.split()
    return [' '.join(words[i:i + max_chunk_words]) for i in range(0, len(words), max_chunk_words)]

def extract_full_sentence(context, start, end):
    before = context[:start]
    after = context[end:]
    before_sent = re.split(r'[.?!]', before)[-1]
    after_sent = re.split(r'[.?!]', after)[0]
    return (before_sent + context[start:end] + after_sent).strip()

def ask_question_from_doc(question, context):
    if not context or len(context.strip().split()) < 50:
        return "**Error:** Document too short for question answering."

    chunks = split_context(context, max_chunk_words=250)
    best_score = 0
    best_answer = ""
    best_sentence = ""

    try:
        for chunk in chunks:
            result = qa_pipeline(question=question, context=chunk)
            answer = result.get("answer", "").strip()
            score = result.get("score", 0.0)

            if score > best_score and answer.lower() not in ["n/a", "none", ""]:
                best_score = score
                best_answer = answer
                start = result.get("start", 0)
                end = result.get("end", 0)
                best_sentence = extract_full_sentence(chunk, start, end)

        if not best_answer:
            return "**Answer:** 🤔 No confident answer found."

        gen_input = f"question: {question} context: {best_sentence}"
        gen_output = gen_qa_pipeline(gen_input, max_new_tokens=100)[0]['generated_text']

        return (
            f"**Answer:** {gen_output.strip()}\n\n"
            f"**Confidence:** {round(best_score * 100, 2)}%\n\n"
            f"**Justified From:** _{best_sentence}_"
        )

    except Exception as e:
        return f"❌ Q&A Error: {str(e)}"

def get_justification_snippet(answer, context):
    sentences = context.split(".")
    answer_emb = semantic_model.encode(answer, convert_to_tensor=True)
    best_score = 0
    best_sent = ""
    for sent in sentences:
        sent = sent.strip()
        if sent:
            sent_emb = semantic_model.encode(sent, convert_to_tensor=True)
            score = util.pytorch_cos_sim(answer_emb, sent_emb).item()
            if score > best_score:
                best_score = score
                best_sent = sent
    if answer.lower() in best_sent.lower():
        start = best_sent.lower().find(answer.lower())
        end = start + len(answer)
        highlighted = best_sent[:start] + f"**{best_sent[start:end]}**" + best_sent[end:]
    else:
        highlighted = best_sent or "No strong support found."
    return highlighted, best_score

def generate_logic_questions(document_text):
    if not document_text or len(document_text.split()) < 80:
        return GENERIC_QUESTIONS
    words = document_text.split()
    trimmed_text = " ".join(words[:700])
    prompt = (
        "Generate exactly 5 logic-based and comprehension-focused questions "
        "based ONLY on the content of the academic text below. Do NOT answer them.\n\n"
        f"{trimmed_text}\n\nQuestions:\n1."
    )
    try:
        result = text_gen(prompt)[0]['generated_text']
        raw = result.split("Questions:")[-1]
        lines = raw.strip().split("\n")

        questions = []
        for line in lines:
            line = line.strip()
            if line.lower().startswith("question"):
                line = line.split(":", 1)[-1].strip()
            if line and (line[0].isdigit() or line.startswith("-")):
                q = line.lstrip("1234567890.- ").strip()
                if "?" in q and len(q.split()) > 3:
                    questions.append(q)
            if len(questions) >= 3:
                break
        if len(questions) < 3:
            questions += random.sample(GENERIC_QUESTIONS, 3 - len(questions))
        return questions
    except Exception as e:
        print("⚠️ Question generation error:", str(e))
        return GENERIC_QUESTIONS

def evaluate_user_answer(document_text, question, user_answer):
    """Compares user answer with model's answer using semantic similarity and gives nuanced feedback."""
    if not document_text or len(document_text.strip().split()) < 50:
        return "⚠️ Document too short to evaluate."

    try:
        expected = qa_pipeline(question=question, context=document_text)["answer"]
        emb_expected = semantic_model.encode(expected, convert_to_tensor=True)
        emb_user = semantic_model.encode(user_answer, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(emb_user, emb_expected).item()

        if similarity >= 0.8:
            return f"✅ Excellent! Your answer is very accurate.\n\n**Expected:** {expected}\n**Similarity:** {round(similarity * 100, 2)}%"
        elif similarity >= 0.6:
            return f"🟡 Good attempt! You’re mostly right.\n\n**Expected:** {expected}\n**Similarity:** {round(similarity * 100, 2)}%"
        elif similarity >= 0.4:
            return f"🔍 Almost there. Your answer is close, but lacks detail.\n\n**Expected:** {expected}\n**Similarity:** {round(similarity * 100, 2)}%"
        else:
            return f"❌ Not quite. Here’s what the document says:\n\n**Expected:** {expected}\n**Similarity:** {round(similarity * 100, 2)}%"
    except Exception as e:
        return f"❌ Evaluation Error: {str(e)}"
