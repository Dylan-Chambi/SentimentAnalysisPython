import time
from src.utils.functions import ms_to_hhmmssms
from src.schemas.sentiment import Sentiment
from src.schemas.complete_analyze import CompleteAnalize, InnerSentiment
from src.predictors.general_predictor import GeneralPredictor
from src.predictors.general_analyzer import GeneralAnalyzer


def analyze_sentiment_from_text(text: str, sentiment_analyzer: GeneralAnalyzer) -> Sentiment:
    start_time = time.time()
    
    category, score = sentiment_analyzer.analyze_sentiment(text)

    inference_time = time.time() - start_time

    inference_time_formatted = ms_to_hhmmssms(inference_time * 1000)

    return Sentiment(
        category=category,
        score=score,
        inference_time_s=inference_time,
        inference_time_formatted=inference_time_formatted,
        text_analyzed=text,
        model=""
    )

def complete_analysis_from_text(text: str, sentiment_analyzer: GeneralAnalyzer, analyzer_predictor: GeneralPredictor) -> CompleteAnalize:
    start_time = time.time()
    pos, ner, emb = analyzer_predictor.analyze_text(text)
    category, score = sentiment_analyzer.analyze_sentiment(text)

    inference_time = time.time() - start_time

    inference_time_formatted = ms_to_hhmmssms(inference_time * 1000)

    return CompleteAnalize(
        models=[""],
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