from pydantic import BaseModel
from .sentiment_category import SentimentCategory
from pydantic import Field

class Sentiment(BaseModel):
    category: SentimentCategory = Field(...)
    score: float = Field(..., ge=-1, le=1)