from mammals import Mammals


class Flying(Mammals):
    def __init__(self, species: str, place_of_living: list, an_endangered_species: bool, mammals_subtype: str,
                 eats_meal: bool, speed: float, winter_migration: bool, color_of_feathers: list):
        super().__init__(species, place_of_living, an_endangered_species, mammals_subtype,
                         eats_meal, speed)
        self.__winter_migration = winter_migration
        self.__color_of_feathers = color_of_feathers

    @property
    def winter_migration(self):
        """
        A method to get information if flying mammal is wintering bird
        """
        return self.__winter_migration

    @winter_migration.setter
    def winter_migration(self, is_winter_migration_type: bool):
        """
        A method to update an information if flying mammal is wintering bird
        """
        self.__winter_migration = is_winter_migration_type

    def migration_location(self, migration_location: str):
        """
        A method to get the migration location of a flying mammal is not a wintering bird
        """
        if not self.__winter_migration:
            print('we winter at home')
        elif not migration_location:
            print('Empty value is not supported for migration location')
        else:
            print(f'{migration_location} - the place where we will spend the winter')

    @property
    def color_of_feathers(self):
        """
        A method to get the color of a bird's feathers
        """
        return self.__color_of_feathers

    @color_of_feathers.setter
    def color_of_feathers(self, new_color_of_feathers: str):
        """
        A method to update the color of a bird's feathers
        """
        if new_color_of_feathers:
            self.__color_of_feathers = new_color_of_feathers
        else:
            print('Empty value is not valid for the color of a birds feathers')

    def add_color_of_feathers(self, add_color_of_feathers: str):
        """
        A method to  add the color of a bird's feathers
        """
        if add_color_of_feathers in self.__color_of_feathers:
            print(f'{add_color_of_feathers} is already exist')
        else:
            self.__color_of_feathers.append(add_color_of_feathers)


if __name__ == '__main__':
    lark = Flying('Mammals', ['Ukraine', 'Poland'], False, 'flying mammals', False, 100, True, ['White'])
    print(lark.winter_migration)
    lark.migration_location('Afrika')
    lark.migration_location('')
    print(lark.winter_migration)
    print(lark.color_of_feathers)
    lark.add_color_of_feathers('Black')
    print(lark.color_of_feathers)
