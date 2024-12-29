pwd = input("what is the master password? ")

#user is picking wheter they want to add or view previous passwords
while True:
    mode = input("would you like to add new passwords or view previous passwords? (view/add)? Press Q to quit").lower()
    if mode == "q":
        break
    if mode == "view":
        pass
    elif mode == "add":
        pass
    else:
        print("Invalid mode. ")
        continue

