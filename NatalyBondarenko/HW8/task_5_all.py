def all_function(sequence: iter) -> bool:
    """
    An alternative to the all function
    """
    for element in sequence:
        if not element:
            return False
    return True


# function verification
names = ('Rik', 'Morty', 'Bart', 'Flanders', 'Alfred')
names2 = ('Rik', 'Morty', '', 'Flanders', 'Alfred')
print(all_function(names))
print(all_function(names2))
