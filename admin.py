import main


def admin_login():
    while True:
        inputUN = input("Enter your admin name:")
        inputPwd = input("Enter you password:")
        print("Admin Login:")
        if (inputUN == "admin" and inputPwd == "123"):
            admin_menu()
        else:
            print("Invalid login!")
            admin_login()


def hall_management():
    print("Hall management")
    print("1) Enter Hall Information")
    print("2) View all the hall information")
    print("3) Search the hall information")
    print("4) Edit the hall information")
    print("5) Delete the hall information")
    choice = input("Enter your choice: ")
    if choice == '1':
        pass
    elif choice == '2':
        pass
    elif choice == '3':
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    else:
        print("Invalid!")
        hall_management()


def booking_management():
    print("Booking management")
    print("1) View all booking information")
    print("2) Search the booking information using the username or email ")
    print("3) Edit booking information")
    print("4) Delete/Cancel the booking information ")
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
        booking_management()


def user_management():
    print("User management")
    print("1) View all the user information")
    print("2) Search user information using the first or last name")
    print("3) Edit the user information")
    print("4) Delete the user from login")
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
        user_management()


def admin_menu():
    while True:
        print("Admin Menu:")
        print("----------------")
        print("1) Hall management")
        print("2) Booking management")
        print("3) User management")
        print("4) Go back to main menu")
        print("----------------")
        choice = input("Enter your choice: ")
        if choice == '1':
            hall_management()
        elif choice == '2':
            booking_management()
        elif choice == '3':
            user_management()
        elif choice == '4':
            main.main()
        else:
            print("Invalid!")
            admin_menu()
