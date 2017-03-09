import os
import random
import sys

random_num = random.randrange(0, 101)

while(random_num != 15):
    print random_num
    random_num = random.randrange(0, 101)
if random_num == 15:
    print (random_num, "<--Here--")

i = 0
while(i <= 20):
    if(i % 2 == 0):
        print i
    elif(i == 9):
        break
    else:
        i += 1
        continue
    i += 1
raw_input()
