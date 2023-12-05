from pydantic import BaseModel
from .sentiment_category import SentimentCategory
from pydantic import Field

class Sentiment(BaseModel):
    category: SentimentCategory = Field(...)
    score: float = Field(..., ge=-1, le=1)
    inference_time_s: float = Field(..., ge=0)
    inference_time_formatted: str = Field(...)
    text_analyzed: str = Field(...)
    model: str = Field(...)