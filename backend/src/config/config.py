from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    
    api_name: str = "NLP sentiment analysis API"
    revision: str = "local"
    spacy_model: str = "es_core_news_md"
    sentiment_model: str = "./src/models/multilingual-sentiment"
    log_level: str = "DEBUG"
    openai_key: str = ""
    gpt_model: str = "gpt-4"
    csv_path: str = "./src/data/data.csv"

@cache
def get_settings() -> Settings:
    return Settings()