import time
from transformers import pipeline
from .general_predictor import GeneralAnalyzer
from src.schemas.sentiment import Sentiment
from src.utils.functions import sentiment_selector, ms_to_hhmmssms

class SentimentAnalyzer(GeneralAnalyzer):
    def __init__(self):
        self.model = pipeline(model="lxyuan/distilbert-base-multilingual-cased-sentiments-student", top_k=None)

    def analyze_sentiment(self, text) -> Sentiment:
        start_time = time.time()

        prediction = self.model(text)[0]
        
        positive_index = next((i for i, item in enumerate(prediction) if item['label'] == 'positive'), None)
        negative_index = next((i for i, item in enumerate(prediction) if item['label'] == 'negative'), None)

        positive_score = prediction[positive_index]["score"]
        negative_score = prediction[negative_index]["score"]

        sentiment_score = positive_score - negative_score

        inference_time = time.time() - start_time

        inference_time_formatted = ms_to_hhmmssms(inference_time * 1000)

        sentiment_category = sentiment_selector(sentiment_score)

        return Sentiment(
            category=sentiment_category, 
            score=sentiment_score, 
            inference_time_s=inference_time, 
            inference_time_formatted=inference_time_formatted, 
            text_analyzed=text, 
            model=""
        )

