import spacy
import numpy as np
from src.predictors.general_predictor import GeneralPredictor
from src.config.config import get_settings

SETTINGS = get_settings()

class SpacyPredictor(GeneralPredictor):
    def __init__(self):
        super().__init__(model_name=SETTINGS.spacy_model, model=spacy.load(SETTINGS.spacy_model))

    def analyze_text(self, text: str) -> tuple:
        doc = self.model(text)
        pos_tagging = [(token.text, token.pos_) for token in doc]
        ner = [(ent.text, ent.label_) for ent in doc.ents]
        embeddings = np.array(doc.vector)
        return pos_tagging, ner, embeddings.tolist()