n = int(input("Enter the number of employees: "))
employees = {}

for i in range(n):
      name = input("Enter the name of the employee: ")
      salary = int(input("Enter the salary: "))
      employees[name] = salary

print("-----------------------------------")
print("----You can now see the salary-----")
print("-----------------------------------")

while True:
      name = input("Enter the name of the employee: ")
      salary = employees.get(name, -1)
      if salary == -1:
            print("Employee does not exist...")
      else :
            print("The salary of the employee is: ", salary)
      choice = input("Do you want to continue?...[Yes/No]")
      if choice == 'No':
            break
