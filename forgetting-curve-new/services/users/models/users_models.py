from pydantic import BaseModel, validator, Field
from datetime import datetime
from typing import Literal, List, Union



class GetUserModel(BaseModel):
    nickname: str = Field(max_length=20)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    age: int = Field(ge=0,le=99)
    job: str = Field(max_length=100)


class StatusUserModel(BaseModel):
    status: Literal['success']


class GetUserModel404(BaseModel):
    detail: Literal['User not found']


class UserModel400(BaseModel):
    loc: List[Union[str, int]]
    msg: str

class HTTPValidationError(BaseModel):
    detail: List[UserModel400]

