from services.users.endpoints import Endpoints
from services.users.payload import PayLoad
from requests import Response
import requests
import allure

class Users:

    def __init__(self):
        self.endpoints = Endpoints
        self.payload = PayLoad


    @allure.step('Отправляю GET запрос на получение списка всех пользователей')
    def get_all_users(self) -> Response:
        response = requests.get(
            url=self.endpoints.get_users()
        )
        return response


    @allure.step('Отправляю GET запрос на получение конкретного пользователя')
    def get_user_by_nickname(self, nickname: str) -> Response:
        response = requests.get(
            url=self.endpoints.get_user_by_nickname(nickname)
        )
        return response


    @allure.step('Отправляю POST запрос на создание пользователя')
    def post_user(self, **kwargs) -> Response:
        response = requests.post(
            url=self.endpoints.post_user(),
            json=self.payload.post_user(**kwargs)
        )
        return response


    @allure.step('Отправляю PUT запрос на обновление данных пользователя')
    def put_user(self, nickname, **kwargs) -> Response:
        response = requests.put(
            url=self.endpoints.put_user(nickname),
            json=self.payload.put_user(**kwargs)
        )
        return response


    @allure.step('Отправляю DELETE запрос на удаление пользователя')
    def delete_user(self, nickname: str) -> Response:
        response = requests.delete(
            url=self.endpoints.delete_user(nickname)
        )
        return response


