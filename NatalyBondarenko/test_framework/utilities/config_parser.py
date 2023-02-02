import configparser
from NatalyBondarenko.test_framework.CONSTANTS import ROOT_DIR

config = configparser.RawConfigParser()
config.read(f'{ROOT_DIR}/configurations/configuration.ini')


class ReadConfig:

    @staticmethod
    def get_base_url():
        return config.get('app_info', 'base_url')

    @staticmethod
    def get_user_name():
        return config.get('user_info', 'user_name')

    @staticmethod
    def get_locked_out_user_name():
        return config.get('user_info', 'locked_out_user_name')

    @staticmethod
    def get_password():
        return config.get('user_info', 'password')

    @staticmethod
    def get_browser_id():
        return config.get('browser', 'browser_id')

    @staticmethod
    def get_first_name():
        return config.get('checkout_info', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('checkout_info', 'last_name')

    @staticmethod
    def get_zip():
        return config.get('checkout_info', 'zip')
