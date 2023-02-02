# Convert string to a dictionary
string = "name=Amanda=sssss&age=32&&salary=1500&currency=euro"
string_modification = string.replace('=sssss&', ' ').replace('&&', ' ').replace('&', ' ')

dictionary = dict(subString.split("=") for subString in string_modification.split(" "))

print(f'Dictionary :  {dictionary}')
