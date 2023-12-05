from abc import ABC
from src.schemas.sentiment import Sentiment


class GeneralAnalyzer(ABC):
    def __init__(self, model_name: str):
        self.model_name = model_name

    def analyze_sentiment(self, text) -> Sentiment:
        pass