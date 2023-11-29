def login():
    while True:
        inputUN = input("Enter your username:")
        inputPwd = input("Enter you password:")
        print("Admin Login:")
        file = open("users.txt")
        data = file.read()
        if(inputUN in data and inputPwd in data):
            print("user_menu()")
        else:
            print("Invalid login!")
            login()