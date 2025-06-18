from endpoints.base_endpoint import BaseEndpoint
import random


class UserEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()
        self.endpoint_name = 'users'


    def get_user(self,nickname:str ='') -> dict:
        """
        Метод для получения списка пользователей, либо одного конкретного,
        отсутствие параметра nickname = получить всех пользователей.
        Возвращает словарь с пользователями и их полями
        """
        self.get(self.endpoint_name, nickname)
        return self.get_json()


    def create_user(self,payload: dict) -> 'UserEndpoint':
        """
        Метод отправляет запрос на создание пользователя,
        требует передачи в параметры всех полей
        """
        self.post(self.endpoint_name,payload)
        return self


    def update_user(self,nickname: str, payload: dict) -> 'UserEndpoint':
        """
        Метод отправляет запрос на обновление данных пользователя
        """
        self.put(self.endpoint_name,nickname,payload)
        return self


    def delete_user(self,nickname: str) -> 'UserEndpoint':
        """
        Метод отправляет запрос на удаление пользователя
        """
        self.delete(self.endpoint_name,nickname)
        return self


    def get_random_user(self) -> dict:
        """
        Метод возвращает случайного пользователя из базы данных
        """
        random_user = self.get_user()[random.randint(0, len(self.get_json()) - 1)]
        return random_user

