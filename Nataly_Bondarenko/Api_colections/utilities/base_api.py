import requests

from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.configurations.config_file import BASE_URL, API_KEY


class BaseApi:
    def __init__(self):
        self.__base_url = BASE_URL
        self._headers = {'Accept': 'application/json', 'Content-Type': 'application/json',
                         'Authorization': f'Bearer {API_KEY}'}
        self.__request = requests

    def get(self, url, headers=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.get(f'{self.__base_url}/{url}', headers=headers, params=params)
        return response

    def post(self, url, headers=None, body=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.post(f'{self.__base_url}/{url}', headers=headers, json=body, params=params)
        return response

    def delete(self, url, headers=None, body=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.delete(f'{self.__base_url}/{url}', headers=headers, json=body, params=params)
        return response

    def put(self, url, headers=None, body=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.put(f'{self.__base_url}/{url}', headers=headers, json=body, params=params)
        return response

    def patch(self, url, headers=None, body=None, params=None):
        if headers is None:
            headers = self._headers
        response = self.__request.patch(f'{self.__base_url}/{url}', headers=headers, json=body, params=params)
        return response
