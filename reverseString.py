# # Using Slicing
# s = input("Enter the string: ")
# print(s[::-1])

# # Manually
# s = input("Enter the string: ")
# i = len(s) - 1
# result = ""
# while i >= 0:
#     result = result + s[i]
#     i = i - 1
# print(result)

# # Swaping
# s = input("Enter the string: ")
# s = list(s)
# l = 0
# r = len(s) - 1

# while l <= r:
#       s[l] = s[r]
#       l+=1
#       r-=1
# s = ''.join(s)
# print(s)

# s = "-".join(["a", "b", "c"])
# print(s)

s = input("Enter the string: ")
print(''.join(reversed(s)))