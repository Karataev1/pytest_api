from endpoints.base_endpoint import BaseEndpoint


class SetupDataBaseEndpoint(BaseEndpoint):
    def __init__(self):
        super().__init__()
        self.endpoint_name = 'setup_database'


    def setup_database(self) -> 'SetupDataBaseEndpoint':
        """
        Метод отправляет запрос на создание базы данных
        """
        self.post(self.endpoint_name)
        return self

