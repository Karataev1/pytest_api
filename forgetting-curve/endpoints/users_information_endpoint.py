from endpoints.base_endpoint import BaseEndpoint
import random
import allure


class UserInformationEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()
        self.endpoint_name = 'users'
        self.under_endpoint = 'information'


    @allure.step('Запрашиваю список информации у пользователя')
    def get_user_information(self,nickname:str ='',index=0):
        """
        Метод для получения списка информации у пользователя
        """
        self.get(nickname=nickname)
        if index:
            return self.get_json()[index-1]
        return self.get_json()


    @allure.step('Создаю пользователя')
    def create_user_information(self,nickname: str, payload: dict) -> 'UserInformationEndpoint':
        """
        Метод отправляет запрос на создание информации для пользователя
        """
        self.post(nickname=nickname,payload=payload)
        return self



    @allure.step('Удаляю пользователя')
    def delete_user_information(self,nickname: str, information_id: str) -> 'UserInformationEndpoint':
        """
        Метод отправляет запрос на удаление пользователя
        """
        self.delete(nickname=nickname,obj_id=information_id)
        return self