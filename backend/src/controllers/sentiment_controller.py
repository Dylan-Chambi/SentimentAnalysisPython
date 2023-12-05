import traceback
from fastapi import HTTPException
from src.schemas.sentiment import Sentiment
from src.services.csv_service import CSVService
from src.schemas.complete_analyze import CompleteAnalize
from src.predictors.general_analyzer import GeneralAnalyzer
from src.predictors.general_predictor import GeneralPredictor
from src.schemas.sentiment_request import SentimentRequest
from src.schemas.analyze_request import AnalyzeRequest
from src.services.sentiment_service import analyze_sentiment_from_text, complete_analysis_from_text


def sentiment_analysis(sentiment_request: SentimentRequest, sentiment_analyzer: GeneralAnalyzer, csv_service: CSVService) -> Sentiment:
    try:
        return analyze_sentiment_from_text(sentiment_request.text, sentiment_analyzer, csv_service)
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

def complete_analysis(analyze_request: AnalyzeRequest, sentiment_analyzer: GeneralAnalyzer, analyzer_predictor: GeneralPredictor, csv_service: CSVService) -> CompleteAnalize:
    try:
        data = complete_analysis_from_text(analyze_request.text, sentiment_analyzer, analyzer_predictor, csv_service)
        return data
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Internal Server Error")