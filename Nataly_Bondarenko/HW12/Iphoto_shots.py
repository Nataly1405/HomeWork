from abc import ABC, abstractmethod


# abstraction
class IPhoto_shots(ABC):

    @abstractmethod
    def meet_customers(self):
        pass

    @abstractmethod
    def turn_on_the_camera(self):
        pass

    @abstractmethod
    def make_shots(self):
        pass

    @abstractmethod
    def turn_off_the_camera(self):
        pass

    @abstractmethod
    def say_goodbye_to_customers(self):
        pass
