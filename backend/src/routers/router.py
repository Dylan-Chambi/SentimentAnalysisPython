from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from src.controllers.sentiment_controller import sentiment_analysis, complete_analysis
from src.controllers.reports_controller import get_reports
from src.controllers.status_controller import get_service_status
from src.schemas.status import Status
from src.predictors.general_analyzer import GeneralAnalyzer
from src.predictors.general_predictor import GeneralPredictor
from src.predictors.sentiment_analyzer import SentimentAnalyzer
from src.predictors.gpt_sentiment_analyzer import GPTPredictor
from src.predictors.spacy_predictor import SpacyPredictor
from src.schemas.sentiment_request import SentimentRequest
from src.schemas.analyze_request import AnalyzeRequest
from src.schemas.sentiment import Sentiment
from src.schemas.complete_analyze import CompleteAnalize
from src.services.csv_service import CSVService




def get_sentiment_analyzer() -> GeneralAnalyzer:
    return SentimentAnalyzer()

def get_gpt_sentiment_analyzer() -> GeneralAnalyzer | GeneralPredictor:
    return GPTPredictor()


def get_analyzer_predictor() -> GeneralPredictor:
    return SpacyPredictor()

def get_csv_service():
    return CSVService()


router = APIRouter()

@router.get("/status")
def status() -> Status:
    return get_service_status()

@router.post("/sentiment")
def sentiment(sentiment_request: SentimentRequest = Depends(), sentiment_analyzer: GeneralAnalyzer = Depends(get_sentiment_analyzer), csv_service: CSVService = Depends(get_csv_service)) -> Sentiment:
    return sentiment_analysis(sentiment_request, sentiment_analyzer, csv_service)


@router.post("/analysis")
def analysis(analyze_request: AnalyzeRequest = Depends(), sentiment_analyzer: GeneralAnalyzer = Depends(get_sentiment_analyzer), analyzer_predictor: GeneralPredictor = Depends(get_analyzer_predictor), csv_service: CSVService = Depends(get_csv_service)) -> CompleteAnalize:
    return complete_analysis(analyze_request, sentiment_analyzer, analyzer_predictor, csv_service)

@router.get("/reports", response_class=StreamingResponse)
def reports(csv_service: CSVService = Depends(get_csv_service)) -> StreamingResponse:
    return get_reports(csv_service)

@router.post("/analysis_v2")
def analysis(analyze_request: AnalyzeRequest = Depends(), sentiment_analyzer: GeneralAnalyzer = Depends(get_gpt_sentiment_analyzer), analyzer_predictor: GeneralPredictor = Depends(get_gpt_sentiment_analyzer), csv_service: CSVService = Depends(get_csv_service)) -> CompleteAnalize:
    return complete_analysis(analyze_request, sentiment_analyzer, analyzer_predictor, csv_service)