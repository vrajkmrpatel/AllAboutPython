tpl = (40, 50, 40, "XYZ")
print(tpl)
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index("XYZ"))

# list vs tuple
lst =[67, 34, "XYZ"]
print(type(lst))
tpl1 = tuple(lst)
print(type(tpl1))
print(tpl1) 

my_tuple = (1, 2, 3, 'x', 'y', 'z')
print(my_tuple[0])
print(my_tuple[2])
print(len(my_tuple))
print('a' in my_tuple)
print('x' in my_tuple)