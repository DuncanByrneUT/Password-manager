from cryptography.fernet import Fernet

#loading the key file we created

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key



master_pwd = input("what is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

#encryption key
# write key
'''def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()'''

# functions that we will pass into the while loop
import os

def view():
    if os.path.exists('passwords.txt'):
        with open('passwords.txt', 'r') as f:
            for line in f:
                try:
                    data = line.rstrip()
                    user, passw = data.split("|")
                    print("User:", user, " | Password:", str(fer.decrypt(passw.encode())))
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
        f.write(name + "|" + str(fer.encrypt(pwd.encode()).decode()) +'\n')

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

