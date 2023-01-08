import pytest
import json

from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.CONSTANTS import ROOT_DIR
from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.objects.user_colection import UserApi
from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.utilities.config_parser import Configurations


@pytest.fixture()
def env():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def delete_last_user():
    response = UserApi().get_list_of_users()
    UserApi().delete_user(user_id=response.json()[0]['id'])
