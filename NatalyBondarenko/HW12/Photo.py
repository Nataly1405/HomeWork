from Iphoto_shots import IPhoto_shots
from Ipost_processing import IPost_processing


# inheritance
class PhotoCenter(IPhoto_shots, IPost_processing):
    def __init__(self, number_of_clients: int):
        self.__sorted = False
        self.__camera = False
        if number_of_clients > 0:
            self.__number_of_clients = number_of_clients
        else:
            raise ValueError("Number of the clients can not be less than 1")
        self.__photo_session_price = 150
        self.__number_of_photos = 200

    # encapsulation
    @property
    def number_of_clients(self):
        return self.__number_of_clients

    # encapsulation
    @number_of_clients.setter
    def number_of_clients(self, new_number_of_clients: int):
        if new_number_of_clients < 1:
            print("The number of participants in the photo session cannot be less than 1")
        elif 2 >= new_number_of_clients >= 1:
            print(f'From 1 to 2 people this is individual or couple photo session. '
                  f'The total price for {self.__number_of_photos} will be {self.__photo_session_price}')
        else:
            print(f'From 2 and more people this is a family photo session. '
                  f'The total price for {self.__number_of_photos} will be {self.__photo_session_price * 2}')

    def preparing(self):
        self.meet_customers()
        self.turn_on_the_camera()

    def photo_session(self):
        self.make_shots()
        self.turn_off_the_camera()
        self.say_goodbye_to_customers()

    def post_processing(self):
        self.sort_photos()
        self.send_photos_to_client()
        self.get_money()

    def turn_on_the_camera(self):
        self.__camera = True
        print("Your camera is ready for beautiful shots")

    def turn_off_the_camera(self):
        self.__camera = False
        print("Your camera is off")

    # polymorphism
    def meet_customers(self):
        if 1 == self.__number_of_clients or 2 == self.__number_of_clients:
            print("Hello, nice to meet you")
        else:
            print("Hello, nice to meet you all")

    # polymorphism
    def make_shots(self):
        if 1 == self.__number_of_clients or 2 == self.__number_of_clients:
            print("I did a beautiful individual and joint photos ")
        else:
            print("I did a beautiful photos of your family")

    # polymorphism
    def say_goodbye_to_customers(self):
        if 1 == self.__number_of_clients or 2 == self.__number_of_clients:
            print("It was a pleasure to meet you. Photos will be ready in 4 days")
        else:
            print("It was nice to meet you. Photos will be ready in a week")

    def sort_photos(self):
        self.__sorted = True
        print("Great, all the photos was sorted")

    # polymorphism
    def send_photos_to_client(self):
        if 1 == self.__number_of_clients or 2 == self.__number_of_clients:
            print(f"I'm sending you {self.__number_of_photos} edited pictures")
        else:
            print(f"I'm sending you {self.__number_of_photos} processed pictures of your family")

    # polymorphism
    def get_money(self):
        if 1 == self.__number_of_clients or 2 == self.__number_of_clients:
            print(f'I hope you liked the pictures. You have to pay {self.__photo_session_price}')
        else:
            print(f'I hope you liked the pictures. You have to pay {self.__photo_session_price * 2}')


if __name__ == '__main__':
    customer = PhotoCenter(1)
    customer.preparing()
    customer.photo_session()
    customer.post_processing()
