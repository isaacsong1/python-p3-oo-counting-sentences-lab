#!/usr/bin/env python3

class MyString:
  def __init__(self, value=''):
    self.value = value

  @property
  def value(self):
    return self._value
  
  @value.setter
  def value(self, value):
    if isinstance(value, str):
      self._value = value
    else:
      print("The value must be a string.")
    
  def is_sentence(self):
    return True if self.value[-1] == '.' else False

  def is_question(self):
    return True if self.value[-1] == '?' else False
  
  def is_exclamation(self):
    return True if self.value[-1] == '!' else False
  
  def count_sentences(self):
    value = self.value
    for punctuation in ['!', '?']:
      value = value.replace(punctuation, '.')

    return len([sent for sent in value.split('.') if sent])
  

