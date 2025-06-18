from servises.generate_text import GenerateText as GT
from schemas.user_schema import UserSchema
import random



class PayLoads:

    @staticmethod
    def get_new_user() -> dict:
        """
        Генерирует поля пользователя
        """
        return  {
            "nickname": GT.generate_char(random.randint(1,20)),
            "first_name": GT.generate_char(random.randint(1,20)),
            "last_name": GT.generate_char(random.randint(1,20)),
            "age": random.randint(1,100),
            "job": GT.generate_char(random.randint(1,20))
        }


    @staticmethod
    def generate_new_users(amount):
        """
        Генерирует список пользователей с готовыми полями
        """
        result = []
        for i in range(amount):
            result.append(PayLoads.get_new_user())
        return result


    @staticmethod
    def generate_update_job_and_age(amount) -> dict:
        """
        Генерирует новые значения для полей job и age
        """
        result = []
        for i in range(amount):
            result.append({'age': random.randint(1,99), 'job': GT.generate_char() })
        return result


    @staticmethod
    def generate_update_data():
        user_fields = list(UserSchema.model_fields.keys())
        user_fields.remove('nickname')

        data_index = random.randint(0, len(user_fields) - 1)
        field_name = user_fields[data_index]
        field_type = UserSchema.model_fields[field_name].annotation

        if field_type is str:
            value = GT.generate_char()
        elif field_type is int:
            value = random.randint(1, 100)
        else:
            value = None

        return {field_name: value}

