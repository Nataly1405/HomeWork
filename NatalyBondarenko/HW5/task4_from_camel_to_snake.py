# convert the list from camel to snake
import re

camelFormat = ["FirstItem", "FriendsList", "MyTuple"]
snake_format = []

for name in camelFormat:
    snake_format.append(re.sub('([a-z])([A-Z])', r'\1_\2', name).lower())
print(snake_format)
