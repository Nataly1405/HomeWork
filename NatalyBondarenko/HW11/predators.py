from mammals import Mammals


class Predators(Mammals):
    def __init__(self, species: str, place_of_living: list, an_endangered_species: bool, mammals_subtype: str,
                 eats_meal: bool, speed: float, mass: float):
        super().__init__(species, place_of_living, an_endangered_species, mammals_subtype,
                         eats_meal, speed)
        self.__mass = mass

    @property
    def mass(self):
        """
        A method to get predators mass
        """
        return self.__mass

    @mass.setter
    def mass(self, new_mass: float):
        """
        A method to change predator's mass
        """
        if new_mass > 0:
            self.__mass = new_mass
        else:
            print('negative mass is invalid for predator')

    def mass_increase(self, mass_increase: float):
        """
        A method to increase predator's mass.
        """
        if mass_increase > 0:
            self.__mass += mass_increase
        else:
            print('negative mass is invalid for predator')


if __name__ == '__main__':
    tiger = Predators('Mammals', ['Thailand', 'India'], True, 'predator', True, 200, 90)
    tiger.mass_increase(35)
    tiger.mass_increase(-1)
    tiger.mass_increase(0)
    print(tiger.mass)
