# Find all of the numbers from 1-1000 that have a 3 in them

# task solution using "Comprehension"
numbers_that_have_3_inide = [number for number in range(1, 1000) if '3' in str(number)]
print(numbers_that_have_3_inide)


# task solution using "Generator"
def three_inide_the_num_gen():
    """
    Function return number from 1-1000 that have a 3 in them
    """
    counter = 1
    while counter <= 1000:
        if '3' in str(counter):
            yield counter
        counter += 1


for number in three_inide_the_num_gen():
    print(number)
