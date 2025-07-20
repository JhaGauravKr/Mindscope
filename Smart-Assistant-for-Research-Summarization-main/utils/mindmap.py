import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from graphviz import Digraph
import random

def generate_mindmap(text: str, max_terms: int = 10) -> Digraph:
    """
    Generate a TF-IDF-based mind map graph from the input text.

    Parameters:
    - text (str): Document content.
    - max_terms (int): Maximum number of keywords to use in mind map.

    Returns:
    - Digraph: A Graphviz Digraph object representing the mind map.
    """
    try:
        # Step 1: TF-IDF scoring
        vectorizer = TfidfVectorizer(max_features=50, stop_words='english')
        X = vectorizer.fit_transform([text])
        terms = vectorizer.get_feature_names_out()
        scores = np.asarray(X.sum(axis=0)).flatten()

        # Step 2: Select top keywords
        sorted_indices = scores.argsort()[::-1]
        top_terms = terms[sorted_indices[:max_terms]]

        # Step 3: Build graph
        dot = Digraph()
        root = top_terms[0]
        dot.node(root, root, shape='ellipse', style='filled', color='lightblue')

        children = top_terms[1:6]
        for child in children:
            dot.node(child, child)
            dot.edge(root, child)

        for parent in children:
            second_level = random.sample(
                [t for t in top_terms if t != parent and t != root], k=2
            )
            for sub in second_level:
                dot.node(sub, sub)
                dot.edge(parent, sub)

        return dot

    except Exception as e:
        raise RuntimeError(f"Mind map generation failed: {e}")
