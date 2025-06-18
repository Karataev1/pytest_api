import requests

class BaseEndpoint:
    """
    При наследовании от этого класса, нужно переопределить имя ручки (self.main_url)
    """
    def __init__(self):
        self.response = None
        self.response_json = None
        self.new_endpoint = None
        self.endpoint_name = None
        self.status_code = None
        self.text = None
        self.main_url = 'http://127.0.0.1:8000'


    def get_response(self):
        return self.response


    def get_json(self):
        return self.response_json


    def setup_attributes(self,response):
        self.response = response
        self.response_json = self.response.json()
        self.status_code = self.response.status_code
        self.text = self.response.text


    def post(self,payload=''):
        post = requests.post(f'{self.main_url}/{self.endpoint_name}',json=payload)
        self.setup_attributes(post)
        return self


    def get(self,payload=''):
        get = requests.get(f'{self.main_url}/{self.endpoint_name}/{payload}')
        self.setup_attributes(get)
        return self


    def put(self,obj,payload=''):
        put = requests.put(f'{self.main_url}/{self.endpoint_name}/{obj}',json=payload)
        self.setup_attributes(put)
        return self


    def delete(self,obj):
        delete = requests.delete(f'{self.main_url}/{self.endpoint_name}/{obj}')
        self.setup_attributes(delete)
        return self


