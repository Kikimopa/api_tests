from pydantic import BaseModel

class Delete(BaseModel):
    code: int
    type: str
    message: str