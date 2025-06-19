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
            "age": random.randint(1,99),
            "job": GT.generate_char(random.randint(1,100))
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
    def get_invalid_user_data():
        invalid_data_nickname = [
            GT.generate_char(21),
            GT.generate_char(22),
            GT.generate_char(23),
            GT.generate_char(24),
        ]
        invalid_data_first_name = [
            GT.generate_char(21),
            GT.generate_char(22),
            GT.generate_char(23),
            '',
        ]
        invalid_data_last_name = [
            GT.generate_char(21),
            GT.generate_char(22),
            GT.generate_char(23),
            '',
        ]
        invalid_data_job = [
            GT.generate_char(101),
            GT.generate_char(102),
            GT.generate_char(103),
            '',
        ]
        invalid_data_age = [
            -1, 0, 100, 101
        ]
        invalid_full_list = [

            {
                'nickname': invalid_data_nickname[i],
                'first_name': invalid_data_first_name[i],
                'last_name': invalid_data_last_name[i],
                'age': invalid_data_age[i],
                'job': invalid_data_job[i],
            }
            for i, ii in enumerate(range(4))
        ]
        one_invalid_line = [
            {
                "nickname": invalid_data_nickname[random.randint(0,3)],
                "first_name": 'test_first_name',
                "last_name": 'test_last_name',
                "age": random.randint(1, 99),
                "job": GT.generate_char(random.randint(1, 100))
            },
            {
                "nickname": 'test_name',
                "first_name": invalid_data_first_name[random.randint(0,3)],
                "last_name": 'test_last_name',
                "age": random.randint(1, 99),
                "job": GT.generate_char(random.randint(1, 100))
            },
            {
                "nickname": 'test_name',
                "first_name": 'test_first_name',
                "last_name": invalid_data_last_name[random.randint(0,3)],
                "age": random.randint(1, 99),
                "job": GT.generate_char(random.randint(1, 100))
            },
            {
                "nickname": 'dlinniy_nick_name_123',
                "first_name": 'test_first_name',
                "last_name": 'test_last_name',
                "age": invalid_data_age[random.randint(0,3)],
                "job": GT.generate_char(random.randint(1, 100))
            },
            {
                "nickname": 'dlinniy_nick_name_123',
                "first_name": 'test_first_name',
                "last_name": 'test_last_name',
                "age": random.randint(1, 99),
                "job": invalid_data_job[random.randint(0,3)]
            }
        ]
        result = invalid_full_list + one_invalid_line
        return result


    @staticmethod
    def generate_invalid_user_data():
        """
        Генерирует пользователя с невалидными данными
        """
        return [

        ]


    @staticmethod
    def get_information():
        return {
            "information": "What is QA",
            "explanation": "QA is Quality Assurance that means that we control the quality of product during all steps of developing"
        }


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

