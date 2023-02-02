from typing import Callable, List, Union, Any


def map_function(callback: Callable, sequence: iter) -> iter:
    """
    An alternative to the map function
    """
    return [callback(item) for item in sequence]


# function verification
names = ('Rik', 'Morty')
print(list(map_function(lambda name: name + ' Smith', names)))
print(list(map(lambda name: name + ' Smith', names)))

numbers = (1, 3, 4.5, 7, 0, 33)
print(list(map_function(lambda number: number + 10, numbers)))
print(list(map(lambda number: number + 10, numbers)))
