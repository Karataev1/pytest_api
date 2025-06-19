from endpoints.setup_database_endpoint import SetupDataBaseEndpoint
from endpoints.users_endpoint import UserEndpoint
from endpoints.payloads import PayLoads as pl
from schemas.user_schema import UserSchema
from servises.validation import Validation
import pytest
import allure
import requests
import time


@pytest.fixture
def get_new_user(request):
    new_user = pl.get_new_user()
    create_endpoint = UserEndpoint()
    create_endpoint.create_user(new_user)
    """    time.sleep(1)
        def fin():
            create_endpoint.delete_user(new_user['nickname'])
        request.addfinalizer(fin)"""
    yield new_user['nickname']


