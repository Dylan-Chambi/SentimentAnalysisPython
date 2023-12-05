import spacy
import numpy as np
from src.predictors.general_predictor import GeneralPredictor

class SpacyPredictor(GeneralPredictor):
    def __init__(self):
        super().__init__(spacy.load("es_core_news_md"))

    def analyze_text(self, text: str) -> tuple:
        doc = self.model(text)
        pos_tagging = [(token.text, token.pos_) for token in doc]
        ner = [(ent.text, ent.label_) for ent in doc.ents]
        embeddings = np.array(doc.vector)
        return pos_tagging, ner, embeddings.tolist()