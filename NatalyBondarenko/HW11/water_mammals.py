from mammals import Mammals


class Water(Mammals):
    def __init__(self, species: str, place_of_living: list, an_endangered_species: bool, mammals_subtype: str,
                 eats_meal: bool, speed: float, scale: bool, number_of_fins: int):
        super().__init__(species, place_of_living, an_endangered_species, mammals_subtype,
                         eats_meal, speed)
        self.__scale = scale
        self.__number_of_fins = number_of_fins

    @property
    def scale(self):
        """
        A method to get information if water mammal is scaly
        """
        return self.__scale

    @scale.setter
    def scale(self, is_scaly: bool):
        """
        A method to update an information if water mammal is scaly
        """
        self.__scale = is_scaly

    def integument(self):
        if self.__scale:
            print('I am a fish and my body is scaly')
        else:
            print('I am not a fish and I do not have a scale, but I am a water mammal')

    @property
    def number_of_fins(self):
        """
        A method to get number of fins
        """
        return self.__number_of_fins

    @number_of_fins.setter
    def number_of_fins(self, new_number_of_fins: int):
        """
        A method to update the number of fins
        """
        if new_number_of_fins < 1:
            print(f'{new_number_of_fins}is not valid for water mammals')
        else:
            self.__number_of_fins = new_number_of_fins

    def fish_kosher_verification(self, ):
        """
         A method to verified  if water mammal is kosher
        """
        if self.__scale and self.__number_of_fins:
            print('I am a kosher fish')
        else:
            print('I am not a kosher fish')


if __name__ == '__main__':
    salamon = Water('Mammals', ['Tasmania', 'Australia'], False, 'family of marsupial mammals', False, 25, True, 4)
    salamon.number_of_fins = 6
    print(salamon.number_of_fins)
    salamon.scale = False
    print(salamon.integument())
    print(salamon.fish_kosher_verification())
