from abc import ABC
from src.schemas.sentiment import Sentiment


class GeneralAnalyzer(ABC):
    def __init__(self, model):
        self.model = model

    def analyze_sentiment(self, text) -> Sentiment:
        pass