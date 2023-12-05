from enum import Enum

class ServiceType(str, Enum):
    SENTIMENT_ANALYSIS = "SENTIMENT_ANALYSIS"
    COMPLETE_ANALYSIS = "COMPLETE_ANALYSIS"