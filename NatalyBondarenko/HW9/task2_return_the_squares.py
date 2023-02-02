def squares_generator():
    """
    The function that returns the squares of even elements for the range 0 to 1000000000 inclusive
    """
    counter = 0
    while counter <= 1000000000:
        if counter % 2 == 0:
            yield pow(counter, 2)
        counter += 1


for even_elements in squares_generator():
    print(even_elements)
