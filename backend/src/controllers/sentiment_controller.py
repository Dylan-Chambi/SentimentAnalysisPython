import traceback
from fastapi import HTTPException
from src.schemas.sentiment import Sentiment
from src.predictors.sentiment_analyzer import SentimentAnalyzer
from src.schemas.sentiment_request import SentimentRequest
from src.services.sentiment_service import analyze_sentiment_from_text


def sentiment_analysis(sentiment_request: SentimentRequest, sentiment_analyzer: SentimentAnalyzer) -> Sentiment:
    try:
        return analyze_sentiment_from_text(sentiment_request.text, sentiment_analyzer)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")