from src.schemas.sentiment_category import SentimentCategory

def sentiment_selector(sentiment_score: float) -> SentimentCategory:
    match sentiment_score:
        case sentiment_score if sentiment_score >= -1 and sentiment_score < -0.7:
            return SentimentCategory.MUY_NEGATIVO
        case sentiment_score if sentiment_score >= -0.7 and sentiment_score < -0.4:
            return SentimentCategory.NEGATIVO
        case sentiment_score if sentiment_score >= -0.4 and sentiment_score < -0.1:
            return SentimentCategory.POCO_NEGATIVO
        case sentiment_score if sentiment_score >= -0.1 and sentiment_score < 0.1:
            return SentimentCategory.NEUTRAL
        case sentiment_score if sentiment_score >= 0.1 and sentiment_score < 0.4:
            return SentimentCategory.POCO_POSITIVO
        case sentiment_score if sentiment_score >= 0.4 and sentiment_score < 0.7:
            return SentimentCategory.POSITIVO
        case sentiment_score if sentiment_score >= 0.7 and sentiment_score <= 1:
            return SentimentCategory.MUY_POSITIVO
        case _:
            raise ValueError(f"El valor {sentiment_score} no se encuentra en el rango de -1 a 1")


def ms_to_hhmmssms(ms: float) -> str:
    seconds = int(ms / 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    milliseconds = int(ms % 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}.{milliseconds:03d}"