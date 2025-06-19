from pydantic import BaseModel, validator, Field
from datetime import datetime


class UserSchema(BaseModel):
    nickname: str = Field(max_length=20)
    first_name: str = Field(max_length=20)
    last_name: str = Field(max_length=20)
    age: int = Field(ge=0,le=99)
    job: str = Field(max_length=100)
