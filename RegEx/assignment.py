import re 

def contains_digit(s):
      pattern = r'\d'
      result = re.search(pattern,s)
      if result:
            return True
      else:
            return False

str1 = 'I am a Developer. and this is my daily routine.0'

print(contains_digit(str1))