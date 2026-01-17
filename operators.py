# Arithmetic operators

a,b = 10,5

print("Addition: ",a + b)
print("Subtration: ",a - b)
print("Mul: ",a * b)
print("Div: ",a / b)
print("Mod: ",a % b)
print("Pow: ",a ** b)
print("Floor div: ",a // b)

# Assignment operators
a = b = c= 10
print(a,b,c)
x,y = 10, 5
x += y
print(x)
x *= y
print(x)

# Comparison operators 
x, y = 77, 88
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Logical Operators 
x=20
y=30

print(x == 20 and y == 30)
print(x == 25 or y == 30)
print(not(x == 20 or y == 31))
