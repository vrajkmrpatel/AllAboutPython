n = int(input("Enter the number: "))

for i in range(n+1):
      if i%10 == 0:
            continue
      if i > 100:
            break
      print(i)