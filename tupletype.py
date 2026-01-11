t1=(20,30,20, 'xyz')
# t2=t1

# print(hex(id(t1)))
# print(hex(id(t2)))

tpl1 = (20)
tpl2 = (20,)

print(type(tpl1))
print(type(tpl2))

# t1[2] = 123  # Gives the error

print(t1*3)
print(t1.count(20))
print(t1.index('xyz'))