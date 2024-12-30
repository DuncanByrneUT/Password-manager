
master_pwd = input("what is the master password? ")

# functions that we will pass into the while loop
import os

def view():
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            for line in f:
                try:
                    data = line.rstrip()
                    user, passw = data.split("|")
                    print("User:", user, "Password:", passw)
                except ValueError:
                    print("Error: Incorrect format in file.")
    else:
        print("No password file found.")



def add():
    name = input('Account Name: ')
    pwd = input("Password: ")

    # with helps us open and close the file
    # with the 'a' mode, we are appending something to the end of the file, and will create a new one if none exist
    with open('passwords.txt', 'a') as f:
        # \n is telling the program to end the current line
        f.write(name + "|" + pwd +'\n')

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

