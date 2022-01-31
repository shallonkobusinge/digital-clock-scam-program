# import json
#
# def login(usr):
#     uN = input("Name: ")
#     pW = input("Password: ")
#
#     if uN in usr.keys():
#         if pW == usr[uN]:
#             print("Welcome back.")
#         else:
#             print("Incorrect password.")
#             return False
#     else:
#         print("Hello, new person.")
#         usr[uN] = pW
#
#     writeUsers(usr)
#     return True
#
# def readUsers():
#     try:
#         with open("users.json", "r") as f:
#             return json.load(f)
#     except FileNotFoundError:
#         return {}
#
# def writeUsers(usr):
#     with open("users.json", "w+") as f:
#             json.dump(usr, f)
#
# users = readUsers()
# success = login(users)
#
# while not success:
#     success = login(users)


def get_input():
    first_num = int(input("Enter the first number:      "))
    second_num = int(input("Enter the second number:    "))
    return first_num, second_num


def add():
    x, y = get_input()
    return x + y


def subtract():
    x, y = get_input()
    return x - y


def multiply():
    x, y = get_input()
    return x * y


def divide():
    x, y = get_input()
    return x // y


def errorHandler():
    return "Invalid choice"


choice = int(input("Which operation do you want to carry out "))

operations = {
    1: add,
    2: subtract,
    3: multiply,
    4: divide
}

output = operations.get(choice, errorHandler)()
print(output)