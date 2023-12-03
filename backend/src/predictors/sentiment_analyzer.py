from transformers import pipeline
from .general_predictor import GeneralAnalyzer
from src.schemas.sentiment import Sentiment
from src.schemas.sentiment_category import SentimentCategory
from src.utils.functions import sentiment_selector

class SentimentAnalyzer(GeneralAnalyzer):
    def __init__(self):
        self.model = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", top_k=None)

    def analyze_sentiment(self, text) -> Sentiment:
        prediction = self.model(text)[0]
        
        positive_index = next((i for i, item in enumerate(prediction) if item['label'] == 'positive'), None)
        negative_index = next((i for i, item in enumerate(prediction) if item['label'] == 'negative'), None)

        positive_score = prediction[positive_index]["score"]
        negative_score = prediction[negative_index]["score"]

        sentiment_score = positive_score - negative_score

        return sentiment_selector(sentiment_score)

