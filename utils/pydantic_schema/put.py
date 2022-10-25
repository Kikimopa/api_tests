from pydantic import BaseModel

class Put(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str