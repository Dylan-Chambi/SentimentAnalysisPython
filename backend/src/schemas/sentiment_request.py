from pydantic import BaseModel, validator


class SentimentRequest(BaseModel):
    text: str