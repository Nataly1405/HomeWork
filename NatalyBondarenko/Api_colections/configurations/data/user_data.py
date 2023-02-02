import json


class User:
    def __init__(self, name, gender, email, status, **kwargs):
        self.name = name if 'name' not in kwargs.keys() else kwargs['name']
        self.gender = gender if 'gender' not in kwargs.keys() else kwargs['gender']
        self.email = email if 'email' not in kwargs.keys() else kwargs['email']
        self.status = status if 'status' not in kwargs.keys() else kwargs['status']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def get_dict(self):
        return self.__dict__

    def get_json(self):
        return json.dumps(self.__dict__)

