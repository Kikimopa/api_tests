from pydantic import BaseModel


class GetPet(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags: list
    status: str

class GetUser(BaseModel):
    id : int
    username : str
    firstName: str
    lastName : str
    email : str
    password : str
    phone : str
    userStatus : int

