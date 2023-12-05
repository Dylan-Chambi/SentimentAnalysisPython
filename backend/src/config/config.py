from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="backend/.env")
    
    api_name: str = "NLP sentiment analysis API"
    revision: str = "local"
    spacy_model: str = "es_core_news_md"
    sentiment_model: str = "lxyuan/distilbert-base-multilingual-cased-sentiments-student"
    log_level: str = "DEBUG"
    csv_path: str = "backend/src/data/data.csv"

@cache
def get_settings() -> Settings:
    return Settings()