import sys


def print_function(*args):
    """
    An alternative to the print function
    """
    sys.stdout.write(''.join(map(str, args)) + '\n')


# function verification
print_function((3, 4, 5, 6))
print_function([222, 454, 1, 2])
print_function({'name': 'Flanders', 'age': 55})
print_function(1, '\t', 'Lisa')
