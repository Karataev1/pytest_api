from services.users.models.users_models import GetUserModel,StatusUserModel,GetUserModel404,HTTPValidationError
from pydantic import BaseModel, ValidationError


class ResponseValidator:
    def __init__(self):
        self.validators = {
            'get': lambda response_json: GetUserModel(**response_json),
            'post': lambda response_json: StatusUserModel(**response_json),
            'put': lambda response_json: StatusUserModel(**response_json),
            'delete': lambda response_json: StatusUserModel(**response_json),
            'get_404': lambda response_json: GetUserModel404(**response_json),
            'post_400': lambda response_json: HTTPValidationError(**response_json),
            'put_400': lambda response_json: HTTPValidationError(**response_json),
            'delete_404': lambda response_json: GetUserModel404(**response_json),
        }

    def validate(self, response_json, type_of_validation: str) -> GetUserModel:
        validator = self.validators.get(type_of_validation)

        try:
            return validator(response_json)
        except ValidationError as e:
            raise ValueError(f"Ошибка валидации: {e}") from e