class Wagons:
    def __init__(self, wagon_number: int, passengers: list):
        self.__wagon_number = wagon_number
        self.__passengers = passengers

    @property
    def wagon_number(self):
        return self.__wagon_number

    @wagon_number.setter
    def wagon_number(self, new_wagon_number: int):
        if new_wagon_number == self.__wagon_number:
            print(f"Oops, number {new_wagon_number} the same as was before ")
        elif new_wagon_number < 1:
            print(f'number {new_wagon_number} is  unsupported')
        else:
            self.__wagon_number = new_wagon_number

    @property
    def passengers(self):
        return self.__passengers

    def add_new_passenger(self, passenger_name_and_surname: str):
        if len(self.__passengers) == 10:
            print('Sorry, there are no empty seats left in the wagon')
        elif not passenger_name_and_surname:
            print('Please, enter your name and surname')
        else:
            self.__passengers.extend([passenger_name_and_surname])

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f'Wagon number is: {self.__wagon_number}\n' \
               f'List of passengers: {self.__passengers}'


if __name__ == '__main__':
    my_train = Wagons(4, ['Bob Shnaider', 'Lisa Simpson'])
    print(len(my_train))
    print(my_train)
    my_train.add_new_passenger('')
    my_train.add_new_passenger('Lary Bary')
    print(my_train)
    print(len(my_train))
