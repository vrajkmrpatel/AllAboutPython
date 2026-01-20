class invalidPasswordException(Exception):
    def __init__(self, msg):
        self.msg = msg


def check_password_strength(pwd):
    if len(pwd) < 8:
        raise invalidPasswordException("Enter the password of minimum length of 8")
    else:
        print(pwd)


try:
    password = input("Enter the password of your choice: ")
    check_password_strength(password)
except InvalidPasswordException as message:
    print(message)
