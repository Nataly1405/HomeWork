def is_prime(argument: int):
    """
        Write a function is_prime that takes 1 argument - a number from 2 to 1000
        and returns True if it is a prime number, and False otherwise.
    """
    if argument == 1:
        return False
    if argument == 2:
        return True
    for number in range(2, 1001):
        if argument % number == 0:
            return False
        return True

# print(is_prime(8))
# print(is_prime(2))
# print(is_prime(10))
# print(is_prime(13))
