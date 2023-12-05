from abc import ABC
from src.schemas.sentiment import Sentiment


class GeneralPredictor(ABC):
    def __init__(self, model_name: str, model):
        self.model_name = model_name
        self.model = model

    def analyze_text(text: str):
        pass