numbers = [1, 2, 3, 4, 5, 6]

try:
    idx = int(input(f"Enter an index (0 to {len(numbers) - 1}): "))
    print(numbers[idx])
except IndexError:
    print("Index out of range")
    print(f"Try to add index in range (0 to {len(numbers) - 1})")
print("Code after execution")
      