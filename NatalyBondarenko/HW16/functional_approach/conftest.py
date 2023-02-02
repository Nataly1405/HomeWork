import faker
import pytest
import random

from Project.hillel_python_qa_homeworks.Nataly_Bondarenko.HW16.functional_approach.human import Human


@pytest.fixture()
def create_custom_human_instance():
    def create_human(name: str, age: int, gender: str):
        return Human(name, age, gender)

    return create_human


@pytest.fixture()
def create_invalid_human_name_int():
    return Human(987654, random.randint(1, 99), 'male')


@pytest.fixture()
def create_invalid_human_name_empty():
    return Human('', random.randint(1, 99), 'male')


@pytest.fixture()
def create_invalid_human_age_negative():
    return Human(faker.name(), random.randint(-99, 0), 'female')


@pytest.fixture()
def create_invalid_human_age_str():
    return Human(faker.name(), "blabla", 'female')
