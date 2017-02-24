import os
import random
import sys

def addNumber(fNum, lNum):
	sum = fNum + lNum
	return sum
	
print(addNumber(1,4))
		
def askName():
	print "What is your name?"
	name = sys.stdin.readline()
	return ("Hello " + name)
		
print askName()
raw_input()
