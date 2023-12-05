import time
from src.utils.functions import ms_to_hhmmssms
from src.schemas.sentiment import Sentiment
from src.schemas.service_type import ServiceType
from src.services.csv_service import CSVService, CSVItem
from src.schemas.complete_analyze import CompleteAnalize, InnerSentiment
from src.predictors.general_predictor import GeneralPredictor
from src.predictors.general_analyzer import GeneralAnalyzer
from src.config.config import get_settings

SETTINGS = get_settings()

def analyze_sentiment_from_text(text: str, sentiment_analyzer: GeneralAnalyzer, csv_service: CSVService) -> Sentiment:
    start_time = time.time()
    
    category, score = sentiment_analyzer.analyze_sentiment(text)

    inference_time = time.time() - start_time

    inference_time_formatted = ms_to_hhmmssms(inference_time * 1000)

    sentiment_response = Sentiment(
        category=category,
        score=score,
        inference_time_s=inference_time,
        inference_time_formatted=inference_time_formatted,
        text_analyzed=text,
        model=sentiment_analyzer.model_name
    )

    csv_service.write_csv(
        CSVItem(
            csv_file_name=SETTINGS.csv_path,
            input_text=text,
            prediction_type=ServiceType.SENTIMENT_ANALYSIS,
            prediction=sentiment_response.model_dump_json(),
            datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            execution_time=inference_time_formatted,
            models=[sentiment_analyzer.model_name]
        )
    )

    return sentiment_response

def complete_analysis_from_text(text: str, sentiment_analyzer: GeneralAnalyzer, analyzer_predictor: GeneralPredictor, csv_service: CSVService) -> CompleteAnalize:
    start_time = time.time()
    pos, ner, emb = analyzer_predictor.analyze_text(text)
    category, score = sentiment_analyzer.analyze_sentiment(text)

    inference_time = time.time() - start_time

    inference_time_formatted = ms_to_hhmmssms(inference_time * 1000)

    complete_analize = CompleteAnalize(
        models=[
            sentiment_analyzer.model_name,
            analyzer_predictor.model_name
        ],
        inference_time_s=inference_time,
        inference_time_formatted=inference_time_formatted,
        text_analyzed=text,
        pos_tagging=pos,
        ner=ner,
        embeddings=emb,
        sentiment=InnerSentiment(
            category=category,
            score=score
        )
    )

    csv_service.write_csv(
        CSVItem(
            csv_file_name=SETTINGS.csv_path,
            input_text=text,
            prediction_type=ServiceType.COMPLETE_ANALYSIS,
            prediction=complete_analize.model_dump_json(),
            datetime=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            execution_time=inference_time_formatted,
            models=complete_analize.models
        )
    )

    return complete_analize