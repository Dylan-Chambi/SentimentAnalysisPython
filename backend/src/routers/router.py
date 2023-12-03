from fastapi import APIRouter, Depends
from src.controllers.sentiment_controller import sentiment_analysis
from src.predictors.sentiment_analyzer import SentimentAnalyzer
from src.schemas.sentiment_request import SentimentRequest
from src.schemas.sentiment import Sentiment



def get_sentiment_analyzer() -> SentimentAnalyzer:
    return SentimentAnalyzer()


router = APIRouter()

@router.post("/sentiment")
def predict(sentiment_request: SentimentRequest = Depends(), sentiment_analyzer: SentimentAnalyzer = Depends(get_sentiment_analyzer)) -> Sentiment:
    return sentiment_analysis(sentiment_request, sentiment_analyzer)