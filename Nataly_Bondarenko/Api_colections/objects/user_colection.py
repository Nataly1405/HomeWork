import json
from os import path

from Auto_Lessons.HomeWork.Nataly_Bondarenko.Api_colections.utilities.base_api import BaseApi


class UserApi(BaseApi):
    def __init__(self):
        super().__init__()
        self.__user_url = 'public/v2/users'

    def get_user(self, user_id: int):
        return self.get(f'{self.__user_url}/{user_id}')

    def create_user(self, user_data: dict):
        json_data = json.dumps(user_data)
        response = self.post(url=f'{self.__user_url}', body=user_data)
        return response

    def get_list_of_users(self):
        return self.get(f'{self.__user_url}')

    def update_user(self, user_id: int, user_data: dict):
        response = self.patch(url=path.join(self.__user_url, str(user_id)), body=user_data)
        return response

    # def delete_user(self, user_id: int):
    #     return self.delete(url=f'{self.__user_url}{user_id}')

    def delete_user(self, user_id: int):
        response = self.delete(url=path.join(self.__user_url, str(user_id)))
        return response
