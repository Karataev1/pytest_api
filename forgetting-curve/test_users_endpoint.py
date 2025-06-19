from endpoints.setup_database_endpoint import SetupDataBaseEndpoint
from endpoints.users_endpoint import UserEndpoint
from endpoints.payloads import PayLoads as pl
from schemas.user_schema import UserSchema
from servises.validation import Validation
import pytest
import allure

validator = Validation.validator


class TestForgettingCurve:


    @allure.title('Тест отправляет запрос на получение списка всех пользователей')
    def test_get_all_users(self):
        """
        Тест отправляет запрос на получение списка всех зарегистрированных пользователей
        """
        endpoint = UserEndpoint()
        endpoint.get_user()
        assert endpoint.status_code == 200, endpoint.text


    @allure.title('Тест отправляет запрос на создание пользователя')
    @pytest.mark.parametrize('payload',pl.generate_new_users(4))
    def test_create_user(self,payload):
        """
        Тест отправляет запрос на создание пользователя и проверяет
        его появление в списке пользователей. Проводит валидацию данных до отправки
        и после.
        """
        endpoint = UserEndpoint()
        validator(payload,UserSchema)
        assert endpoint.create_user(payload).status_code == 200, endpoint.text

        new_user = endpoint.get_user(payload['nickname'])
        validator(new_user,UserSchema)
        assert new_user['nickname'] == payload['nickname'], endpoint.text


    @allure.title('Тест отправляет запрос на получение конкретного пользователя и проводит валидацию')
    def test_get_user(self):
        """
        Тест отправляет запрос на получение конкретного пользователя и проводит валидацию
        """
        endpoint = UserEndpoint()
        user = endpoint.get_random_user()
        endpoint.get_user(user['nickname'])
        validator(user,UserSchema)
        assert endpoint.status_code == 200, endpoint.text


    @allure.title('Тест отправляет запрос на обновление данных пользователя')
    @pytest.mark.parametrize('payload', pl.generate_update_job_and_age(4))
    def test_update_user_data(self,payload):
        """
        Тест отправляет запрос на обновление данных пользователя и проверяет
        эти изменения. Проводит валидацию данных после обновления.
        """
        endpoint = UserEndpoint()
        random_user = endpoint.get_random_user()
        assert endpoint.update_user(random_user['nickname'],payload).status_code == 200

        new_user = endpoint.get_user(random_user['nickname'])
        validator(new_user,UserSchema)
        assert  new_user['job'] == payload['job'] and \
                new_user['age'] == payload['age'], \
                endpoint.text


    @allure.title('Тест отправляет запрос на удаление пользователя')
    def test_delete_user(self):
        """
        Тест отправляет запрос на удаление пользователя и проверяет
        его отсутствие в списке пользователей.
        """
        endpoint = UserEndpoint()
        random_user = endpoint.get_random_user()
        assert endpoint.delete_user(random_user['nickname']).status_code == 200, endpoint.text

        endpoint.get_user(random_user['nickname'])
        assert endpoint.status_code == 404, endpoint.text


    @allure.title('Тест отправляет запрос на создание пользователя с невалидными данными')
    @pytest.mark.negative
    @pytest.mark.parametrize('payload',pl.get_invalid_user_data())
    def test_create_user_invalid_data(self,payload):
        """
        Тест отправляет запрос на создание пользователя с невалидными данными и
        проверяет наличие ошибки 400
        """
        endpoint = UserEndpoint()
        assert endpoint.create_user(payload).status_code == 400, endpoint.text

        endpoint.get_user(payload['nickname'])
        assert endpoint.status_code == 404, endpoint.text


if __name__=='__main__':
    endpoint_ = UserEndpoint()
    #endpoint_.create_user(pl.get_new_user())
    #print(pl.new_generate_update_data())
    #print(endpoint_.get_users().get_json())
    print(pl.get_invalid_user_data()[7]['nickname'])

