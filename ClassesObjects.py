import os
import random
import sys

class Animal:
  __name = ""
  __height = 0
  __weight = 0
  __sound = ""
  
  def __init__(self, name, height, weight, sound):
    self.__name = name
    self.__height = height
    self.__weight = weight
    self.__sound = sound
  
  def set_name(self , name):
	if (type(name) != str ):
		raise TypeError("Please use a string")
	self.__name = name
    
  def get_name(self):
    return self.__name
    
  def set_height(self , height):
    self.__height = height
    
  def get_height(self):
    return self.__height
    
  def set_weight(self , weight):
    self.__weight = weight
    
  def get_weight(self):
    return self.__weight
    
  def set_sound(self , sound):
	if (type(sound) != str ):
		raise TypeError("Please use a string")
    self.__sound = sound
    
  def get_sound(self):
    return self.__sound

