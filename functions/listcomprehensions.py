lst = [1, 2, 3, 4, 5, 6, 7]

# Using map
# cube = list(map(lambda x: x**3, lst))
# print(cube)

# lst = [x**3 for x in lst]
# print(lst)

# even number between 1 and 20
# lst = [x for x in range(2,21,2)]
# lst = [x for x in range(1,21) if x%2==0]
# print(lst)

# Product of two lists
a = [1, 2, 3, 4, 5]
b = [2, 3, 4, 5, 6]

z = []
# for i in range(len(a)):
#       z.append(a[i]*b[i])

# z = [a[i]*b[i] for i in range(len(a))]

# common element in a and b
'''for i in a:
      if i in b:
            z.append(i)'''

z = [i for i in a if i in b]
print(z)