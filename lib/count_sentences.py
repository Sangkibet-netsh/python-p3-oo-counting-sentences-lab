#!/usr/bin/env python3

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