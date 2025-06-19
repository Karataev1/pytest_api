from pydantic import BaseModel
from typing import Type
import allure



class Validation:


    @staticmethod
    @allure.step('Провожу валидацию')
    def validator(payload: dict, schema: Type[BaseModel]) -> BaseModel:
        return schema(**payload)
