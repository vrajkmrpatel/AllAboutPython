# ATM Program
import sys

balance = 10000

print("-----Welcom to ATM-----")
print("---Choose the ooption from below---")
print("1. Check Balance")
print("2. WithDraw")
print("3. Deposit Cash")
print("4. Deposit Check")
print("5. Quit")


if len(sys.argv) < 2:
    print("Please provide an action (1-5) as a command-line argument.")
    sys.exit(1)

try:
    choice = int(sys.argv[1])
except ValueError:
    print("Invalid argument! Please provide an integer (1-5).")
    sys.exit(1)

match choice:
    case 1:
        print(f"Your Balance is: {balance}")
    case 2:
        if len(sys.argv) < 3:
            print("Please provide the withdrawal amount as a command-line argument.")
            sys.exit(1)
        try:
            withdraw = int(sys.argv[2])
            if withdraw > balance:
                print("Insufficient funds!")
            else:
                balance -= withdraw
                print(f"Transaction Processing... Here is your money: {withdraw}")
        except ValueError:
            print("Invalid withdrawal amount. Please provide an integer.")
            sys.exit(1)
    case 3:
        if len(sys.argv) < 3:
            print("Please provide the deposit amount as a command-line argument.")
            sys.exit(1)
        try:
            deposit = int(sys.argv[2])
            balance += deposit
            print("Your amount has been deposited.")
        except ValueError:
            print("Invalid deposit amount. Please provide an integer.")
            sys.exit(1)
    case 4:
        if len(sys.argv) < 3:
            print(
                "Please provide the deposit amount via check as a command-line argument."
            )
            sys.exit(1)
        try:
            deposit = int(sys.argv[2])
            balance += deposit
            print("Your check deposit has been processed.")
        except ValueError:
            print("Invalid deposit amount. Please provide an integer.")
            sys.exit(1)
    case 5:
        print("Thank you for using the ATM! Goodbye.")
        sys.exit(0)
    case _:
        print("Invalid choice! Please choose a valid option (1-5).")
        sys.exit(1)
