from pydantic import BaseModel, validator, Field

class Post(BaseModel):
    id: int
    category: dict
    name: str
    photoUrls: list
    tags : list
    status : str



    # @validator("id")
    # def check_id_less_onetwothree(cls, v):
    #     if v > 123:
    #         raise ValueError("ID is not less than 2")
    #     else:
    #         return v