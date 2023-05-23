#!/usr/bin/env python3
import re
class MyString:
  def __init__(self, value = ''):
        self._value = value
        
  def get_value(self):
      return self._value

  def set_value(self, value):
      if (type(value) == str):
          print(f"Setting value to {value}")
          self._value = value
      else:
          print("The value must be a string.")

  value = property(get_value, set_value)

  def is_sentence(self):
        return self._value.endswith(".")
  
  #The endswith() method is a built-in string method in Python that is used to check whether a string ends with a specified suffix or sequence of characters.
  def is_question(self):
        return self._value.endswith("?")
  
  def is_exclamation(self):
        return self._value.endswith("!")
  
  def count_sentences(self):
        if self.value == '':
            return 0
        else:
            return len(re.split(r'[!\?\.](?= )', self.value))
        

# The 're' module is the regular expression module in 
# Python, which provides functions for working with 
# regular expressions. Regular expressions are powerful 
# tools for pattern matching and string manipulation.