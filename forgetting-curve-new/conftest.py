import pytest
from services.users.api_users import Users
from services.users.payload import PayLoad as pl
from services.users.models.validation import ResponseValidator


@pytest.fixture()
def users():
    return Users()


@pytest.fixture()
def validation_response():
    return ResponseValidator()


@pytest.fixture()
def create_user(users):
    """
    Фикстура создает пользователя и возвращает его никнейм, после отправляет запрос на его удаление
    :return: data['nickname']
    """
    data = pl.post_user(
            nickname='FixtureCreateUser',
            first_name='first_name',
            last_name='last_name',
            age=19,
            job='non job'
        )
    users.post_user(
        **data
    )
    yield data
    users.delete_user(data['nickname'])