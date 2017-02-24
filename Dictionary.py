import os
import random
import sys

super_villains = { 1 : 'Mean Guy', 2 :'Nice Guy' , 3 : 'Kinda Nice Guy'}
del super_villains[2]

print super_villains
print len(super_villains)
print super_villains.get(1)
print super_villains.keys()
print super_villains.values()
raw_input()