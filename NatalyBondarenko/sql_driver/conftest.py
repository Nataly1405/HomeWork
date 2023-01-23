import json

import psycopg2
import pytest

from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.CONSTANTS import ROOT_DIR
from Auto_Lessons.HomeWork.NatalyBondarenko.sql_driver.utilities.configurations import Configurations


@pytest.fixture()
def env1():
    with open(f'{ROOT_DIR}/configurations/configurations.json') as file:
        env_dict = json.loads(file.read())
    return Configurations(**env_dict)


@pytest.fixture()
def create_connection(env1):
    connection = psycopg2.connect(
        user=env1.user,
        password=env1.password,
        host=env1.host,
        port=env1.port,
        database=env1.database
    )
    yield connection
    connection.close()
