prime_flag = True

n = int(input("Enter the number: "))

for i in range(2, n - 1):
      if n % i == 0:
            prime_flag = False

if (prime_flag):
      print("Prime Number")
else :
      print("No a Prime Number")
