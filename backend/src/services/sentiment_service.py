from src.schemas.sentiment import Sentiment
from src.predictors.sentiment_analyzer import SentimentAnalyzer


def analyze_sentiment_from_text(text: str, sentiment_analyzer: SentimentAnalyzer) -> Sentiment:
    return sentiment_analyzer.analyze_sentiment(text)