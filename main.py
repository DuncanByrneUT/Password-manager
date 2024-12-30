pwd = input("what is the master password? ")

# functions that we will pass into the while loop
def view():
    pass
def add():
    name = input('Account Name: ')
    acct_pwd = input("Password: ")

    # with helps us open and close the file
    # with the 'a' mode, we are appending something to the end of the file, and will create a new one if none exist
    with open('passwords.txt', 'a') as f:
        # \n is telling the program to end the current line
        f.write(name + "|" + acct_pwd +'\n')




#user is picking wheter they want to add or view previous passwords
while True:
    mode = input("would you like to add new passwords or view previous passwords? (view/add)? Press Q to quit: ").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode. ")
        continue

