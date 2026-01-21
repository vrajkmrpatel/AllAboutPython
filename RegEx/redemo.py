

'''
      Sequence Characters

      \d - digit
      \D - non digit
      \s - space
      \S - non spaces
      \w - alphanumeric value
      \W - non alphanumeric
      \b - space around words
      \A - matches at the start of the string
      \Z - matches at the end of the string
'''

import re 

str = "Take 1 up 1-12-1998 One 45 idea.One idea 93 at a time Only 12-11-2011"
# result = re.search(r'o\w\w', str)
# print(result.group())

# result = re.findall(r'o\w\w', str)
# print(result)

# result = re.match(r'T\w\w\w', str)
# print(result.group())

# result = re.sub(r'one','two', str)
# print(result)

# result = re.split(r'\d+', str)
# print(result)


'''
      Quantifiers

      + -> one or more 
      \d+ --> one or more digits 

      * --> zero or more

      ? --> zero or one 

      {m} --> exactly m occurances
      {m,n} --> min m and max n occurances 

'''

# result = re.findall(r'O\w+', str)
# print(result)

# result = re.findall(r'O\w{3}', str)
# print(result)

result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', str)
print(result)