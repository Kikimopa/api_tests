from pydantic import BaseModel


class Get(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str

