import os
import random
import sys
  
class Animal(object):
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
  
  def get_type(self):
    print("Animal")
  
  def toString(self):
    return "{} is {} cm tall and {} kilograms, and says {}".format(
                                                                    self.get_name(),
                                                                    self.get_height(),
                                                                    self.get_weight(),
                                                                    self.get_sound())
cat = Animal('Cuck', 33,10,'Meow')

print(cat.toString())


class Dog(Animal):
  __owner = ""
  
  def __init__(self, name, height, weight, sound, owner):
    self.__owner = owner
    super(Dog, self).__init__(name, height, weight, sound)
    
  def set_owner(self, owner):
    self.__owner = owner
    
  def get_owner(self):
    return self.__owner
  
  def get_type(self):
    print("Dog")
    
  def toString(self):
    return "{} is {} cm tall and {} kilograms, says {} and owner is {}".format(
                                                                    self.get_name(),
                                                                    self.get_height(),
                                                                    self.get_weight(),
                                                                    self.get_sound(),
                                                                    self.__owner)

  def multiple_sounds(self, how_many=None):
    if how_many is None:
      print(self.get_sound())
    else:
      print(self.get_sound() * how_many)


spot = Dog("Spot", 53, 27, "Ruff", "Donray")

print(spot.toString())

class AnimalTesting:
	def get_type(self, animal):
	 animal.get_type()
 
test_animals = AnimalTesting()
 
test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds(4)
spot.multiple_sounds()
raw_input()

