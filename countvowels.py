word = input("Enter the string: ") # eagle
vowels = ['a', 'e','i','o','u']

results = {}
for c in word:
      if c in vowels:
            results[c] = results.get(c, 0) + 1
# print(results)
for k, v in results.items():
      print(k,"appears",v,"times")


