# import sys

# lst = sys.argv

# for i in lst: print(i)
# print(len(lst))
# print(lst[0])

# Product of command line argument
import sys

lst = sys.argv
prod = 1
for i in range(1, len(lst)):
      prod *= int(lst[i])
print("Product is:",prod)