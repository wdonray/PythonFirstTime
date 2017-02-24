import os
import random
import sys

test_file = open("test.txt", "ab+")

print test_file.mode

print test_file.name

test_file.write("Write me to the file")

test_file.close()

os.remove("test.txt")
raw_input()
