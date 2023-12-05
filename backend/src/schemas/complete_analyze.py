from pydantic import BaseModel
from pydantic import Field
from src.schemas.sentiment_category import SentimentCategory

class InnerSentiment(BaseModel):
    category: SentimentCategory = Field(...)
    score: float = Field(..., ge=-1, le=1)

class CompleteAnalize(BaseModel):
    models: list[str] = Field(...)
    inference_time_s: float = Field(..., ge=0)
    inference_time_formatted: str = Field(...)
    text_analyzed: str = Field(...)
    pos_tagging: list[tuple[str, str]] = Field(...)
    ner: list[tuple[str, str]] = Field(...)
    embeddings: list[float] = Field(...)
    sentiment: InnerSentiment = Field(...)