
from pydantic import BaseModel


class PosTagging(BaseModel):
    pos_tagging: list[tuple[str, str]]