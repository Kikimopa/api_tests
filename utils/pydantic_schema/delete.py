from pydantic import BaseModel

class DeletePet(BaseModel):
    code: int
    type: str
    message: str