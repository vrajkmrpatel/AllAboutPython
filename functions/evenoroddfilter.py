lst = [1, 2, 3, 4, 5, 6, 7]

# filter(function, list)

result = list(filter(lambda x:x%2 == 0, lst))
print(result)