import os
import random
import sys

name = "Donray"
quote = "I matter"

print("%s %s" %(name, quote))
print(name, quote)
print('\n' * 2)

number_list = [1,2,3,4]
word_list = ["Donray","Max"]
both_list = ["Donray" , 1]

all_list = [number_list,word_list,both_list]

print("First Item", number_list[0])
print('\n')
print number_list[1:4]
print('\n')
all_list.append(2)
all_list.sort()
del all_list[3]
print(all_list)
print(len(all_list))
print(max(all_list))


raw_input()