s = 'aaabbbbbccccIIZZZZ'

result = []
for c in s:
      if c not in result:
            result.append(c)
print(result)
output = ''.join(result)
print(output)