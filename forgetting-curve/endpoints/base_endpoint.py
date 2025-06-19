import requests
from pydantic import BaseModel
from typing import Type
import allure


class BaseEndpoint:
    """
    При наследовании от этого класса, нужно переопределить имя ручки (self.endpoint_name)
    """
    def __init__(self):
        self.main_url = 'http://127.0.0.1:8000'

        self.response = None
        self.response_json = None
        self.new_endpoint = None
        self.endpoint_name = ''
        self.under_endpoint = ''
        self.status_code = None
        self.text = None


    def get_response(self):
        return self.response


    def get_json(self):
        return self.response_json


    @allure.step('Получаю ответ от API')
    def setup_attributes(self,response):
        self.response = response
        self.response_json = self.response.json()
        self.status_code = self.response.status_code
        self.text = self.response.text


    @allure.step('Отправляю POST запрос')
    def post(self,payload='', nickname=''):
        if not nickname  == '': nickname += '/'
        post = requests.post(f'{self.main_url}/{self.endpoint_name}/{nickname}{self.under_endpoint}',json=payload)
        self.setup_attributes(post)
        return self


    @allure.step('Отправляю GET запрос')
    def get(self,nickname=''):
        get = requests.get(f'{self.main_url}/{self.endpoint_name}/{nickname}/{self.under_endpoint}')
        self.setup_attributes(get)
        return self


    @allure.step('Отправляю PUT запрос')
    def put(self,nickname,payload=''):
        put = requests.put(f'{self.main_url}/{self.endpoint_name}/{nickname}/{self.under_endpoint}',json=payload)
        self.setup_attributes(put)
        return self


    @allure.step('Отправляю DELETE запрос')
    def delete(self,nickname,obj_id=''):
        if not obj_id == '': obj_id = '/' + obj_id
        delete = requests.delete(f'{self.main_url}/{self.endpoint_name}/{nickname}/{self.under_endpoint}{obj_id}')
        print(f'{self.main_url}/{self.endpoint_name}/{nickname}/{self.under_endpoint}{obj_id}')
        self.setup_attributes(delete)
        return self





