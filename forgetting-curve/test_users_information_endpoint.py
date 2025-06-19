import pytest, allure
from endpoints.users_information_endpoint import UserInformationEndpoint
from endpoints.users_endpoint import UserEndpoint
from endpoints.payloads import PayLoads as pl
from conftest import get_new_user as user


class TestUsersInformationEndpoint:


    @allure.step('Тест запрашивает информацию у пользователя и валидирует данные')
    def test_get_user_information(self,user):

        new_info = pl.get_information()
        endpoint = UserInformationEndpoint()
        assert endpoint.create_user_information(user,new_info).status_code == 200, endpoint.text
        info = endpoint.get_user_information(user,1)
        assert new_info['information'] == info['information'] and new_info['explanation'] == info['explanation']
        assert endpoint.delete_user_information(user, '1').status_code == 200, endpoint.text



    @allure.step('Тест удаляет информацию у пользователя')
    def test_delete_user_information(self):
        endpoint = UserInformationEndpoint()
        assert endpoint.delete_user_information('cvvpbjfsaabvcfde','2').status_code == 200, endpoint.text