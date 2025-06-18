from endpoints.setup_database_endpoint import SetupDataBaseEndpoint
from endpoints.users_endpoint import UserEndpoint
from payloads import PayLoads as pl
from schemas.user_schema import UserSchema
from servises.validation import Validation
import pytest
import allure
import random

validator = Validation.validator


class TestForgettingCurve:


    def test_setup_database(self):
        """
        Тест отправляет запрос на создание базы данных и проверяет успешность процедуры
        """
        endpoint = SetupDataBaseEndpoint()
        with allure.step('Отправляю запрос на создание базы данных'):
            endpoint.setup_database()
        with allure.step('Ожидаю статус код 200'):
            assert endpoint.status_code == 200


    def test_get_all_users(self):
        """
        Тест отправляет запрос на получение списка всех зарегистрированных пользователей
        """
        endpoint = UserEndpoint()
        with allure.step('Отправляю запрос на получение списка всех зарегистрированных пользователей'):
            endpoint.get_user()
        with allure.step('Ожидаю статус код 200'):
            assert endpoint.status_code == 200, endpoint.text


    @pytest.mark.parametrize('payload',pl.generate_new_users(4))
    def test_create_user(self,payload):
        """
        Тест отправляет запрос на создание пользователя и проверяет
        его появление в списке пользователей. Проводит валидацию данных до отправки
        и после.
        """
        endpoint = UserEndpoint()
        with allure.step('Создаю макет нового пользователя и провожу валидацию'):
            #payload = pl.get_new_user()
            validator(payload,UserSchema)
        with allure.step(f'Отправляю запрос на создание нового пользователя ({payload['nickname']})'):
            endpoint.create_user(payload)
        with allure.step('Ожидаю статус код 200'):
            assert endpoint.status_code == 200, endpoint.text
        with allure.step('Отправляю запрос на получение данных о последнем созданном пользователе и провожу валидацию'):
            new_user = endpoint.get_user(payload['nickname'])
            validator(new_user,UserSchema)
        with allure.step('Проверяю успешное создание нового пользователя'):
            assert new_user['nickname'] == payload['nickname'], endpoint.text


    @pytest.mark.parametrize('payload', pl.generate_update_job_and_age(4))
    def test_update_user_data(self,payload):
        """
        Тест отправляет запрос на обновление данных пользователя и проверяет
        эти изменения. Проводит валидацию данных до отправки
        и после.
        """
        endpoint = UserEndpoint()
        with allure.step('Создаю макет json для обновления данных. Генерирую новые данные'):
            random_user = endpoint.get_random_user()
        with allure.step(f'Отправляю запрос на обновление случайного пользователя ({random_user['nickname']} | {payload})'):
            endpoint.update_user(random_user['nickname'],payload)
        with allure.step('Ожидаю статус код 200'):
            assert endpoint.status_code == 200
        with allure.step('Отправляю запрос на получение данных об обновляемом пользователе и провожу валидацию'):
            new_user = endpoint.get_user(random_user['nickname'])
            validator(new_user,UserSchema)
        with allure.step('Проверяю успешное обновление данных пользователя'):
            assert  new_user['job'] == payload['job'] and \
                    new_user['age'] == payload['age'], \
                    endpoint.text


    def test_delete_user(self):
        """
        Тест отправляет запрос на удаление пользователя и проверяет
        его отсутствие в списке пользователей.
        """
        endpoint = UserEndpoint()
        with allure.step('Выбираю случайного пользователя для удаления'):
            random_user = endpoint.get_random_user()
        with allure.step(f'Отправляю запрос на удаление пользователя ({random_user['nickname']})'):
            endpoint.delete_user(random_user['nickname'])
        with allure.step('Ожидаю статус код 200'):
            assert endpoint.status_code == 200, endpoint.text
        with allure.step('Отправляю запрос на получение данных об удаленном пользователе'):
            endpoint.get_user(random_user['nickname'])
        with allure.step('Проверяю его отсутствие в списке всех пользователей'):
            assert endpoint.status_code == 404, endpoint.text


if __name__=='__main__':
    endpoint_ = UserEndpoint()
    #endpoint_.create_user(pl.get_new_user())
    #print(pl.new_generate_update_data())
    #print(endpoint_.get_users().get_json())
    print(type(endpoint_.get_random_user()))

