import allure

main_url = 'http://127.0.0.1:8000'

class Endpoints:


    @staticmethod
    def get_users():
        url = f'{main_url}/users'
        return url


    @staticmethod
    def get_user_by_nickname(nickname: str):
        url = f'{main_url}/users/{nickname}'
        return url


    @staticmethod
    def post_user():
        url = f'{main_url}/users'
        return url


    @staticmethod
    def put_user(nickname):
        url = f'{main_url}/users/{nickname}'
        return url


    @staticmethod
    def delete_user(nickname):
        url = f'{main_url}/users/{nickname}'
        return url