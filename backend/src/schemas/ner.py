from pydantic import BaseModel

class NER(BaseModel):
    ner: list[tuple[str, str]]