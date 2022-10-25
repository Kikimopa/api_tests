from pydantic import BaseModel

class PutPet(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str