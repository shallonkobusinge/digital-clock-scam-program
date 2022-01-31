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

#
# def get_input():
#     first_num = int(input("Enter the first number:      "))
#     second_num = int(input("Enter the second number:    "))
#     return first_num, second_num
#
#
# def add():
#     x, y = get_input()
#     return x + y
#
#
# def subtract():
#     x, y = get_input()
#     return x - y
#
#
# def multiply():
#     x, y = get_input()
#     return x * y
#
#
# def divide():
#     x, y = get_input()
#     return x // y
#
#
# def errorHandler():
#     return "Invalid choice"
#
#
# choice = int(input("Which operation do you want to carry out "))
#
# operations = {
#     1: add,
#     2: subtract,
#     3: multiply,
#     4: divide
# }
#
# output = operations.get(choice, errorHandler)()
# print(output)


from tkinter import*
root = Tk()
root.geometry('500x500')
root.title(" Login ")
credentials = open("credentials.txt", mode="a+", encoding="utf-8")
def getValue():
    username_value = entry_1.get()
    password_value = entry_2.get()
    credentials.write("Username " + username_value + "\n")
    credentials.writelines("Password " + password_value + "\n")
    print(username_value)
    print(password_value)
    credentials.close()


label_0 = Label(root, text="Kikuu now has great discount offers Login and check it out! ",width=50,font=("bold", 13))
label_0.place(x=45,y=53)
label_1 = Label(root, text="Username",width=20,font=("bold", 12))
label_1.place(x=80,y=130)
entry_1 = Entry(root)
entry_1.place(x=240,y=130)
label_2 = Label(root, text="Password",width=20,font=("bold", 12))
label_2.place(x=68,y=180)
entry_2 = Entry(root)
entry_2.config(show="*")
entry_2.place(x=240,y=180)
Button(root, text='Submit',width=20,bg='blue',fg='white', command=getValue).place(x=180,y=220)


root.mainloop()
print("registration form  seccussfully created...")