from pydantic import BaseModel

class SentimentScore(BaseModel):
    score: float