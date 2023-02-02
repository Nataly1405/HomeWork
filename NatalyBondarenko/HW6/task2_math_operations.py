# Using the created file in task 1, read the file and perform mathematical operations on each element.
# Output the result of the operation to the console.
# You cannot use imports to import from the first task module.

with open('test/data/list_of_tuple.txt') as file:
    tuples_list = file.readlines()

tuples_list_split = []
for element in tuples_list:
    tuples_list_split.append(element.replace("\n", "").split(" "))

# print(tuples_list_split)

for item in tuples_list_split:
    if item[1] == "1":
        print(f'The sum of the right and left operands = {int(item[0]) + int(item[2])}')
    elif item[1] == "2":
        print(f'The subtraction of the right and left operands = {int(item[0]) - int(item[2])}')
    elif item[1] == "3":
        print(f'The multiplication of the right and left operands = {int(item[0]) * int(item[2])}')
