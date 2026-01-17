lst =[20,30,40,50]
print(type(lst))
# print(lst)

b = bytes(lst)
print(type(b))
# print(b)

# b[3] = 22

b1 = bytearray(lst)
print(type(b1))
print(b1)

b1[2] = 33
print(b1)