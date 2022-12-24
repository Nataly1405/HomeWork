from abc import ABC, abstractmethod


# abstraction
class IPost_processing(ABC):

    @abstractmethod
    def sort_photos(self):
        pass

    @abstractmethod
    def send_photos_to_client(self):
        pass

    @abstractmethod
    def get_money(self):
        pass
