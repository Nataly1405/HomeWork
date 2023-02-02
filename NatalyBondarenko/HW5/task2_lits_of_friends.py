# print each name on a new line, right-aligned (using f string metod).
# in the first line, display the headings Names
# where the word names should be in the middle(rest space "*")

list_of_friends = ["John", "Marta", "James", "Amanda", "Marianna"]

print('Names'.center(len('Names') + 10, '*'))

for friend in list_of_friends:
    print(f'{friend:>10}')
