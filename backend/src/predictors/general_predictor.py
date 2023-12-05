from abc import ABC
from src.schemas.sentiment import Sentiment


class GeneralPredictor(ABC):
    def __init__(self, model):
        self.model = model

    def analyze_text(text: str):
        pass