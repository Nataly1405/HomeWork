from http import HTTPStatus

import requests

from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.configurations.config_file import API_KEY
from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.configurations.data.user_data import User
from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.objects.user_colection import UserApi
from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.conftest import delete_last_user


def test_get_user():
    response = UserApi().get_user(271)
    print(response.json())
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


def test_get_list_of_users():
    response = UserApi().get_list_of_users()
    print(response.json())
    assert response.status_code == HTTPStatus.OK, f'Status code is not as expected\n Actual: {response.status_code}' \
                                                  f'\nExpected: {HTTPStatus.OK}'


# Fail because of "delete_last_user" - doesn't work
def test_create_user(delete_last_user, env):
    delete_last_user
    new_user = User(env.name1, env.gender1, env.email1, env.status)
    response = UserApi().create_user(new_user.get_dict())
    assert response.status_code == HTTPStatus.CREATED, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.CREATED}'


# google recommendations :)
# def test_get_first_user():
#     response = UserApi().get_list_of_users()
#     print(response.json())
#     # response = requests.get("https://gorest.co.in/public/v2/users")
#     users = response.json()
#     first_user_id = response.json()[0]['id']
#     print(first_user_id)
#     # assert first_user_id["id"] == 4329
#     assert first_user_id["name"] == "Bob Mayls"
#     api_url = f"https://gorest.co.in/public/v2/users/{first_user_id}"
#     headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
#                'Authorization': f'Bearer {API_KEY}'}
#     response = requests.delete(api_url, headers=headers)
#     assert response.status_code == 200 or response.status_code == 204


# Doesn't work because of `response.json()[0]['id']`
def test_update_existing_user():
    update_user = {
        "name": "Grinch3",
        "gender": "male",
        "email": "grinch3@gmail.com",
        "status": "active"}
    response = UserApi().get_list_of_users()
    response = UserApi().update_user(user_id=response.json()[0]['id'], user_data=update_user)
    assert response.status_code == HTTPStatus.OK, f"Status code not expected\nExpected: {HTTPStatus.OK}" \
                                                  f"\nActual: {response.status_code}"


def test_update_not_existing_user():
    update_user = {
        "name": "Elf",
        "gender": "male",
        "email": "santahelper@gmail.com",
        "status": "active"}
    response = UserApi().update_user(user_id=123456789, user_data=update_user)
    assert response.status_code == HTTPStatus.NOT_FOUND, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.NOT_FOUND}'


def test_get_user_404():
    response = UserApi().get_user(0)
    assert response.status_code == HTTPStatus.NOT_FOUND, f"Unexpected status code\nExpected: {HTTPStatus.NOT_FOUND}\n" \
                                                         f"Actual: {response.status_code}"


def test_delete_user_404(env):
    response = UserApi().delete_user(0)
    assert response.status_code == HTTPStatus.NOT_FOUND, f'User cannot have id = 0, must be error: ' \
                                                         f'{HTTPStatus.NOT_FOUND} - not found'


def test_create_existing_person(env):
    existing_user = User(env.name1, env.gender1, env.email1, env.status)
    response = UserApi().create_user(existing_user.get_dict())
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
        f'Status code is not as expected\n Actual: {response.status_code}' \
        f'\nExpected: {HTTPStatus.UNPROCESSABLE_ENTITY}'


# Doesn't work because of `response.json()[0]['id']`
def test_delete_existing_person():
    response = UserApi().get_list_of_users()
    response = UserApi().delete_user(user_id=response.json()[0]['id'])
    assert response.status_code == HTTPStatus.NO_CONTENT, f'Status code is not as expected\n ' \
                                                          f'Actual: {response.status_code}' \
                                                          f'\nExpected: {HTTPStatus.NO_CONTENT}'


def test_keys():
    response = UserApi().get_list_of_users()
    person_keys = response.json()[0].keys()
    dict_keys = {'id': '', 'name': '', 'email': '', 'gender': '', 'status': ''}
    assert person_keys == dict.keys(dict_keys), f'Dictionary keys are incorrect'
