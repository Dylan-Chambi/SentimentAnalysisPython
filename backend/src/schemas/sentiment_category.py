from enum import Enum

class SentimentCategory(str, Enum):
    MUY_NEGATIVO = "Muy negativo"
    NEGATIVO = "Negativo"
    POCO_NEGATIVO = "Poco negativo"
    NEUTRAL = "Neutral"
    POCO_POSITIVO = "Poco positivo"
    POSITIVO = "Positivo"
    MUY_POSITIVO = "Muy positivo"