from pydantic import BaseModel, validator
from datetime import datetime

class UserSchema(BaseModel):
    nickname: str
    first_name: str
    last_name: str
    age: int
    job: str
