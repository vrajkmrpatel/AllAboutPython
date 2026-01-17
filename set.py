s = {10, 20, 30, "XYZ", 10, 20}
# print(s)
# print(type(s))

s.update([88,99])
print(s)
print(type(s))

# print(s[0]) 

# print(s*3)
s.remove(30)
print(s)

# frozen set
f = frozenset(s)
# f.update([20])
# f.remove(20)
print(f)