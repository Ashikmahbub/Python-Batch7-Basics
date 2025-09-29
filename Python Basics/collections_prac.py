import collections

from collections import defaultdict, namedtuple, deque

fuits = ['apple', 'banana', 'orange', 'apple', 'orange', 'banana', 'apple']


fruit_counter = collections.Counter(fuits)
print(fruit_counter)

fruit_dict = defaultdict(int)
for fruit in fuits:
    fruit_dict[fruit] += 1
print(fruit_dict)