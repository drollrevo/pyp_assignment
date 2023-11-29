def login():
    while True:
        inputUN = input("Enter your admin name:")
        inputPwd = input("Enter you password:")
        print("Admin Login:")
        file = open("users.txt")
        data = file.read()
        if(inputUN in data and inputPwd in data):
            admin_menu()
        else:
            print("Invalid login!")
            login()

def admin_menu():
    while True:
        print("Admin Menu:")
        print("----------------")
        print("1) Enter Hall Information")
        print("2) View all the hall information")
        print("3) Search the hall information")
        print("4) Go back to main menu")
        choice = input("Enter your choice: ")
        if choice == '1':
            pass
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            pass
        else:
            print("Invalid!")
            admin_menu()