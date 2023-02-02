# Please count how many times each letter appears in this file
from collections import Counter
import re

with open('text.txt', 'r') as file:
    data = file.read()

data_updated = re.sub(r'(\W+)|(\d+)', r'', data)

result = Counter(data_updated)
print(result)
