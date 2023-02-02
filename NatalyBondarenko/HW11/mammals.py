from animals import Animal


class Mammals(Animal):
    def __init__(self, species: str, place_of_living: list, an_endangered_species: bool, mammals_subtype: str,
                 eats_meal: bool, speed: float):
        super().__init__(species, place_of_living, an_endangered_species)
        self.__mammals_subtype = mammals_subtype
        self.__eats_meal = eats_meal
        self.__speed = speed

    @property
    def mammals_subtype(self):
        """
        A method to get mammals subtype
        """
        return self.__mammals_subtype

    @mammals_subtype.setter
    def mammals_subtype(self, new_mammals_subtype: str):
        """
        A method to update mammals subtype
        """
        if new_mammals_subtype:
            self.__mammals_subtype = new_mammals_subtype
        else:
            print('Empty value is not valid for mammals subtype')

    @property
    def eats_meal(self):
        """
        A method to get an information what an animal eats
        """
        return self.__eats_meal

    @eats_meal.setter
    def eats_meal(self, is_eats_meal: bool):
        """
        A method to update an information what an animal eats
        """
        self.__eats_meal = is_eats_meal

    def predators(self):
        """
        A method to check if the animal is predator
        """
        if not self.__eats_meal:
            print('Oh no, I do not eat my friends')
        else:
            print("I am a predator and I love fresh meat")

    @property
    def speed(self):
        """
        A method to get animal speed
        """
        return self.__speed

    @speed.setter
    def speed(self, speed_value: float):
        """
        A method to update animal speed
        """
        if speed_value >= 1:
            self.__speed = speed_value
        else:
            print(f'{speed_value} - this speed is not valid for animals speed value')

    def speed_increase(self, speed_increase: int):
        """
        A method to increase animal speed
        """
        if speed_increase < 1:
            print(f'{speed_increase} is unsupported value for speed increase')
        else:
            self.__speed += speed_increase


if __name__ == '__main__':
    kangaroo = Mammals('Mammals', ['Tasmania', 'Australia'], False, 'family of marsupial mammals', False, 50)

    print(kangaroo.mammals_subtype)
    kangaroo.eats_meal = True
    print(kangaroo.predators())
    print(kangaroo.speed)
    kangaroo.speed_increase(25)
    print(kangaroo.speed)
