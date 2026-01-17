x = int(input("Enter the 1st number"))
y = int(input("Enter the 2nd number"))

i = x
if i%2 == 0:
      i+=1
while i <= y:
    print(i)
    i += 2
