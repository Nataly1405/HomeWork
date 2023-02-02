from typing import Callable


def filter_function(callback: Callable, sequence: iter) -> iter:
    """
    An alternative to the filter function
    """
    return [item for item in sequence if callback(item)]


# function verification
numbers = (1, 3, 4.5, 7, 0, 33)

print(list(filter_function(lambda number: number > 2, numbers)))
print(list(filter(lambda number: number > 2, numbers)))
