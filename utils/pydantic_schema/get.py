from pydantic import BaseModel


class GetPet(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str

