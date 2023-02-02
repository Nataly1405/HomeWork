# Find all of the numbers from 1-1000 that are divisible by 7

# task solution using "Comprehension"
numbers_divisible_by_7 = [number for number in range(1, 1000) if number % 7 == 0]
print(numbers_divisible_by_7)


# task solution using "Generator"
def divisible_by_7_gen():
    """
    Function return numbers from 1-1000 that are divisible by 7
    """
    counter = 1
    while counter <= 1000:
        if counter % 7 == 0:
            yield counter
        counter += 1


for number in divisible_by_7_gen():
    print(number)
