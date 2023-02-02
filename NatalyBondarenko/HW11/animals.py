class Animal:
    def __init__(self, species: str, place_of_living: list, an_endangered_species: bool):
        self.__species = species
        self.__place_of_living = place_of_living
        self.__an_endangered_species = an_endangered_species

    @property
    def species(self):
        """
        A method to get animal species
        """
        return self.__species

    @species.setter
    def species(self, new_species_value: str):
        """
        A method to update the animal species
        """
        if new_species_value:
            self.__species = new_species_value
        else:
            print('Empty value is not valid for animal species')

    @species.deleter
    def species(self):
        """
        A method to protect code against class design break
        """
        pass

    @property
    def place_of_living(self):
        """
        A method to get animal species
        """
        return self.__place_of_living

    @place_of_living.setter
    def place_of_living(self, new_living_place_value: str):
        """
        A method to add new animals living place
        """
        if new_living_place_value in self.__place_of_living:
            print(f'{new_living_place_value} is already in the animals living place list')
        elif not new_living_place_value:
            print('Empty value is not valid for animals living place')
        else:
            self.__place_of_living.append(new_living_place_value)

    def to_remove_place_of_living(self, place_to_remove: str):
        """
        A method to remove the place of animal living
        """
        if place_to_remove in self.__place_of_living:
            return self.__place_of_living.remove(place_to_remove)
        else:
            print(f'{place_to_remove} can not be find in the animals living place list')

    @property
    def an_endangered_species(self):
        """
        A method to get information if it is an endangered species
        """
        return self.__an_endangered_species

    @an_endangered_species.setter
    def an_endangered_species(self, is_an_endangered_species: bool):
        """
        A method to update information if it is an endangered species
        """
        self.__an_endangered_species = is_an_endangered_species

    def an_endangered_species_verification(self):
        """
        A method to verified if it is an endangered species
        """
        if not self.__an_endangered_species:
            print('this species is not threatened with extinction')
        else:
            print('This species is on the verge of extinction. '
                  'Additional protection of this specie is needed')


if __name__ == '__main__':
    panda = Animal('Mammals', ['China', 'Japan'], False)
    print(panda.species)
    panda.species = 'Reptiles'
    print(panda.species)
    print(panda.place_of_living)
    panda.place_of_living = 'Nepal'
    print(panda.to_remove_place_of_living('Japan'))
    print(panda.place_of_living)
    panda.an_endangered_species = True
    print(panda.an_endangered_species_verification())
