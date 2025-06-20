from services.users.api_users import Users
import pytest
from conftest import users, create_user, validation_response
from services.users.payload import PayLoad as pl
from services.generate_text import GenerateText as GT
from services.users.models.users_models import GetUserModel
import random



class TestUsers:


    def test_get_users_positive(self, users):
        """
        Тест отправляет запрос на получение всех пользователей в базе данных.
        """
        response = users.get_all_users()
        assert response.status_code == 200, response.json()


    def test_get_user_by_nickname_positive(self, users, create_user, validation_response):
        """
        Тест отправляет запрос на получение конкретного пользователя по nickname,
        проводит валидацию.
        """
        response = users.get_user_by_nickname(create_user['nickname'])
        assert response.status_code == 200, response.json()
        validator = validation_response.validate(response.json(),'get')
        assert validator


    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_nickname',[ GT.generate_char(10) ])
    def test_get_user_by_nickname_negative(self, users, create_user, invalid_nickname, validation_response):
        """
        Тест отправляет запрос на получение конкретного пользователя по nickname,
        проводит валидацию. Предварительно создает пользователя чтобы список пользователей не был пустым.
        Используется несуществующий никнейм.
        """
        response = users.get_user_by_nickname(invalid_nickname)
        assert response.status_code == 404, response.json()
        validator = validation_response.validate(response.json(),'get_404')
        assert validator


    @pytest.mark.parametrize('data', [
        pl.post_user(
            nickname=GT.generate_char(20),
            first_name=GT.generate_char(20),
            last_name=GT.generate_char(20),
            age=1,
            job=GT.generate_char(100)
        ),
        pl.post_user(
            nickname=GT.generate_char(1),
            first_name=GT.generate_char(1),
            last_name=GT.generate_char(1),
            age=99,
            job=GT.generate_char(1)
        )
    ])
    def test_post_user_positive(self, users, data, validation_response):
        """
        Тест отправляет POST запрос на создание пользователя, проводит валидацию ответа.
        Используются граничные значения для всех полей.
        """
        response = users.post_user(**data)
        assert response.status_code == 200, response.json()
        validator = validation_response.validate(response.json(),'post')
        assert validator

    @pytest.mark.negative
    @pytest.mark.parametrize('data',[
        # В этом кейсе отправляется неверный nickname (превышает количество символов >20)
        pl.post_user(nickname=GT.generate_char(21),first_name=GT.generate_char(20),last_name=GT.generate_char(20),age=random.randint(1,99),job=GT.generate_char(100)),
        # В этом кейсе отправляется неверный first_name (превышает количество символов >20)
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(21), last_name=GT.generate_char(20),age=random.randint(1, 99), job=GT.generate_char(100)),
        # В этом кейсе отправляется неверный last_name (превышает количество символов >20)
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name=GT.generate_char(21),age=random.randint(1, 99), job=GT.generate_char(100)),
        # В этом кейсе отправляется неверный age (превышает допустимое значение >99)
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name=GT.generate_char(20),age=100, job=GT.generate_char(100)),
        # В этом кейсе отправляется неверный job (превышает количество символов >100)
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name=GT.generate_char(20),age=random.randint(1, 99), job=GT.generate_char(101)),

        # В этом кейсе отправляется пустая строчка nickname
        pl.post_user(nickname='', first_name=GT.generate_char(20), last_name=GT.generate_char(20),age=random.randint(1, 99), job=GT.generate_char(100)),
        # В этом кейсе отправляется пустая строчка first_name
        pl.post_user(nickname=GT.generate_char(20), first_name='', last_name=GT.generate_char(20),age=random.randint(1, 99), job=GT.generate_char(100)),
        # В этом кейсе отправляется пустая строчка last_name
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name='', age=random.randint(1, 99), job=GT.generate_char(100)),
        # В этом кейсе отправляется неверный age (не входит в допустимые значения <1)
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name=GT.generate_char(20),age=0, job=GT.generate_char(100)),
        # В этом кейсе отправляется пустая строчка job
        pl.post_user(nickname=GT.generate_char(20), first_name=GT.generate_char(20), last_name=GT.generate_char(20),age=random.randint(1, 99), job=''),
    ],ids=['invalid_nickname_chars',
           'invalid_first_name_chars',
           'invalid_last_name_chars',
           'invalid_age_value',
           'invalid_job_chars',     # айдишки у кейсов для валидации ошибки для конкретного случая
           'empty_nickname_field',
           'empty_first_name_field',
           'empty_last_name_field',
           'invalid_age_value',
           'empty_job_field',
           ])
    def test_post_user_negative(self, users, data, validation_response):
        """
        Тест отправляет POST запрос с неверными полями на создание пользователя, проводит валидацию ответа.
        """
        response = users.post_user(**data)
        assert response.status_code == 400, response.json()
        validator = validation_response.validate(response.json(),'post_400')
        assert validator


    @pytest.mark.parametrize('data',[
        pl.put_user(age=1,job=GT.generate_char(1)),
        pl.put_user(age=99, job=GT.generate_char(100)),
    ])
    def test_put_user_positive(self, users, data, create_user, validation_response):
        """
        Тест отправляет PUT запрос на обновление полей age и job пользователя.
        Проводит валидацию ответа.
        """
        response = users.put_user(create_user['nickname'], **data)
        assert response.status_code == 200, response.json()
        validator = validation_response.validate(response.json(), 'put')
        assert validator


    @pytest.mark.negative
    @pytest.mark.parametrize('data',[
        # В этом кейсе передается неверный age (<0)
        pl.put_user(age=0,job=GT.generate_char(1)),
        # В этом кейсе передается неверный job (пустая строка)
        pl.put_user(age=99, job=''),
        # В этом кейсе передается неверный age (>99)
        pl.put_user(age=100, job=GT.generate_char(1)),
        # В этом кейсе передается неверный job (превышено количество символов >100)
        pl.put_user(age=99, job=GT.generate_char(101)),
    ])
    def test_put_user_negative(self, users, data, create_user, validation_response):
        """
        Тест отправляет PUT запрос на обновление полей age и job пользователя используя неверные поля.
        Проводит валидацию ответа.
        """
        response = users.put_user(create_user['nickname'], **data)
        assert response.status_code == 400, response.json()
        validator = validation_response.validate(response.json(), 'put_400')
        assert validator


    def test_delete_user_positive(self, users, create_user, validation_response):
        """
        Тест отправляет DELETE запрос на удаление пользователя.
        Проводит валидацию ответа.
        """
        response = users.delete_user(create_user['nickname'])
        assert response.status_code == 200, response.json()
        validator = validation_response.validate(response.json(), 'delete')
        assert validator


    @pytest.mark.negative
    @pytest.mark.parametrize('invalid_nickname', [GT.generate_char(10)])
    def test_delete_user_negative(self, users, create_user, validation_response, invalid_nickname):
        """
        Тест отправляет DELETE запрос на удаление пользователя с несуществующим никнеймом.
        Предварительно создает пользователя чтобы список пользователей не был пустым.
        Проводит валидацию ответа.
        """
        response = users.delete_user(invalid_nickname)
        assert response.status_code == 404, response.json()
        validator = validation_response.validate(response.json(), 'delete_404')
        assert validator

