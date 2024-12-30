pwd = input("what is the master password? ")

# functions that we will pass into the while loop
def view():
    pass
def add():
    name = input('Account Name: ')


#user is picking wheter they want to add or view previous passwords
while True:
    mode = input("would you like to add new passwords or view previous passwords? (view/add)? Press Q to quit").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue

