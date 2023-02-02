def max_function(sequence: iter, value: int = 1) -> list:
    """
    An alternative to the max function
    """
    sorted_sequence = sorted(sequence, reverse=True)
    return sorted_sequence[:value]


def min_function(sequence: iter, value: int = 1) -> list:
    """
    An alternative to the min function
    """
    sorted_sequence = sorted(sequence, reverse=False)
    return sorted_sequence[:value]


# function verification
numbers = (1, 3, 4.5, 7, 6, 0, 33, 5)
print(max_function(numbers, 2))
print(min_function(numbers, 2))

names = ('Rik', 'Morty', 'Bart', 'Flanders', 'Alfred')
print(max_function(names, 1))
print(min_function(names, 1))
