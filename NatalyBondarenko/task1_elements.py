list_of_elements = [1, 2, 3, 4, 5, 6, 7, 8]
an_odd_index = []
an_even_index = []

for index, value in enumerate(list_of_elements):
    if index % 2 == 1:
        an_odd_index.append((index, value))
    else:
        an_even_index.append((index, value))

print(f'an_odd_index = {an_odd_index} \n', f'an_even_index = {an_even_index}')
