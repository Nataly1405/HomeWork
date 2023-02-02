from typing import Callable


def function_name(func: Callable):
    """
    Returning the names of functions
    """

    def wrapper(*args):
        return f'Function name: {func.__name__}\nFunction result: {func(*args)}'

    return wrapper


@function_name
def summation(number1: float, number2: float) -> float:
    return number1 + number2


@function_name
def multiplication(number1: float, number2: float) -> float:
    return number1 * number2


# function verification
print(summation(2.5, 5))
print(multiplication(5.1, 10))
