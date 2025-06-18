from endpoints.base_endpoint import BaseEndpoint
import random
import allure


class UserEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()
        self.endpoint_name = 'users'


    @allure.step('Запрашиваю список пользователей')
    def get_user(self,nickname:str ='') -> dict:
        """
        Метод для получения списка пользователей, либо одного конкретного,
        отсутствие параметра nickname = получить всех пользователей.
        Возвращает словарь с пользователями и их полями
        """
        self.get(nickname)
        return self.get_json()


    @allure.step('Создаю пользователя')
    def create_user(self,payload: dict) -> 'UserEndpoint':
        """
        Метод отправляет запрос на создание пользователя,
        требует передачи в параметры всех полей
        """
        self.post(payload)
        return self


    @allure.step('Обновляю данные пользователя')
    def update_user(self,nickname: str, payload: dict) -> 'UserEndpoint':
        """
        Метод отправляет запрос на обновление данных пользователя
        """
        self.put(nickname,payload)
        return self


    @allure.step('Удаляю пользователя')
    def delete_user(self,nickname: str) -> 'UserEndpoint':
        """
        Метод отправляет запрос на удаление пользователя
        """
        self.delete(nickname)
        return self


    @allure.step('Получаю случайного пользователя')
    def get_random_user(self) -> dict:
        """
        Метод возвращает случайного пользователя из базы данных
        """
        random_user = self.get_user()[random.randint(0, len(self.get_json()) - 1)]
        return random_user

