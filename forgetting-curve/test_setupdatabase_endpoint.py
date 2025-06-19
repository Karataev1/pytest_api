import allure
from endpoints.setup_database_endpoint import SetupDataBaseEndpoint


class TestSetupDataBaseEndpoint:

    @allure.title('Тест отправляет запрос на создание базы данных')
    def test_setup_database(self):
        """
        Тест отправляет запрос на создание базы данных и проверяет успешность процедуры
        """
        endpoint = SetupDataBaseEndpoint()
        assert endpoint.setup_database().status_code == 200, endpoint.text
