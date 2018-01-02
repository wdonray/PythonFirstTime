import os
import random
import sys

for x in range(1, 11):
    print x
print '\n'

grocery_list = ["Water", "Ice", "Milk"]
for y in grocery_list:
    print y
print '\n'

for x in [2, 3, 4, 5, 6]:
    print x
print '\n'

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]
for x in range(0, 3):
    for y in range(0, 3):
        print num_list[x][y]
raw_input()
