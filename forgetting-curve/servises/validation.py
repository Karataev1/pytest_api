from pydantic import BaseModel
from typing import Type



class Validation:


    @staticmethod
    def validator(payload: dict, schema: Type[BaseModel]) -> BaseModel:
        return schema(**payload)
