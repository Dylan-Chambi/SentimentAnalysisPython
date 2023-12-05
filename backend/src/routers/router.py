from fastapi import APIRouter, Depends
from src.controllers.sentiment_controller import sentiment_analysis, complete_analysis
from src.predictors.general_analyzer import GeneralAnalyzer
from src.predictors.general_predictor import GeneralPredictor
from src.predictors.sentiment_analyzer import SentimentAnalyzer
from src.predictors.spacy_predictor import SpacyPredictor
from src.schemas.sentiment_request import SentimentRequest
from src.schemas.analyze_request import AnalyzeRequest
from src.schemas.sentiment import Sentiment
from src.schemas.complete_analyze import CompleteAnalize



def get_sentiment_analyzer() -> GeneralAnalyzer:
    return SentimentAnalyzer()


def get_analyzer_predictor() -> GeneralPredictor:
    return SpacyPredictor()


router = APIRouter()

@router.post("/sentiment")
def predict(sentiment_request: SentimentRequest = Depends(), sentiment_analyzer: GeneralAnalyzer = Depends(get_sentiment_analyzer)) -> Sentiment:
    return sentiment_analysis(sentiment_request, sentiment_analyzer)


@router.post("/analysis")
def predict(analyze_request: AnalyzeRequest = Depends(), sentiment_analyzer: GeneralAnalyzer = Depends(get_sentiment_analyzer), analyzer_predictor: GeneralPredictor = Depends(get_analyzer_predictor)) -> CompleteAnalize:
    return complete_analysis(analyze_request, sentiment_analyzer, analyzer_predictor)