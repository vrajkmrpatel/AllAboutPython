n = int(input("Enter the number of rows: "))

# right angle triangle

# for i in range(1, n + 1):
#       for j in range(1, i + 1):
#             print("* ", end="")
#       print()

# for i in range(1, n + 1):
#     print("* " * i)

# pyramid triangel
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)
