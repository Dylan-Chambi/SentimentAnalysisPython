from src.schemas.sentiment_category import SentimentCategory
from src.schemas.sentiment import Sentiment

def sentiment_selector(sentiment_score: float) -> Sentiment:
    match sentiment_score:
        case sentiment_score if sentiment_score >= -1 and sentiment_score < -0.7:
            return Sentiment(category=SentimentCategory.MUY_NEGATIVO, score=sentiment_score)
        case sentiment_score if sentiment_score >= -0.7 and sentiment_score < -0.4:
            return Sentiment(category=SentimentCategory.NEGATIVO, score=sentiment_score)
        case sentiment_score if sentiment_score >= -0.4 and sentiment_score < -0.1:
            return Sentiment(category=SentimentCategory.POCO_NEGATIVO, score=sentiment_score)
        case sentiment_score if sentiment_score >= -0.1 and sentiment_score < 0.1:
            return Sentiment(category=SentimentCategory.NEUTRAL, score=sentiment_score)
        case sentiment_score if sentiment_score >= 0.1 and sentiment_score < 0.4:
            return Sentiment(category=SentimentCategory.POCO_POSITIVO, score=sentiment_score)
        case sentiment_score if sentiment_score >= 0.4 and sentiment_score < 0.7:
            return Sentiment(category=SentimentCategory.POSITIVO, score=sentiment_score)
        case sentiment_score if sentiment_score >= 0.7 and sentiment_score <= 1:
            return Sentiment(category=SentimentCategory.MUY_POSITIVO, score=sentiment_score)
        case _:
            raise ValueError(f"El valor {sentiment_score} no se encuentra en el rango de -1 a 1")

