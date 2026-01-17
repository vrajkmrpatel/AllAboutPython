# s = "All the power is with in you"
# temp = s.split()
# print(temp)
# result = []
# i = len(temp) - 1
# while i >= 0:
#       result.append(temp[i])
#       i -= 1
# print(result)
# output = ' '.join(result)
# print(output)

# Reverese the characters in words
s = 'Super Cool Python'
# output: repuS looC nohtyP

lst = s.split()
print(lst)
result = []
i = 0
while i < len(lst):
      result.append(lst[i][::-1])
      i += 1
print(' '.join(result))
