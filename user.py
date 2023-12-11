import main

USERS_FILE = "users.txt"

# Global variable to store user information
users_data = []


# Load existing user data from the file at the beginning
def load_users_data():
    try:
        with open(USERS_FILE, "r") as file:
            for line in file:
                user_dict = eval(line)
                users_data.append(user_dict)
    except FileNotFoundError:
        pass


# Save user data to the file after any modification
def save_users_data():
    with open(USERS_FILE, "w") as file:
        for user_dict in users_data:
            file.write(str(user_dict) + "\n")


def registration():
    print("\nUser Registration:")
    username = input("Enter your username: ")

    # Check if the username is already taken
    while any(user_dict['Username'] == username for user_dict in users_data):
        print("Username already exists. Please choose another one.")
        username = input("Enter your username: ")

    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth: ")
    contact_number = input("Enter your contact number: ")
    email = input("Enter your email address: ")

    # Create a dictionary to represent the user
    user_dict = {
        'Username': username,
        'Password': password,
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': dob,
        'Contact Number': contact_number,
        'Email': email
    }

    # Add the user dictionary to the global list
    users_data.append(user_dict)

    # Save the updated user data to the file
    save_users_data()

    print("Registration successful!\n")


def login():
    main_choice = input("Do you have an account? (yes/no): ")

    if main_choice.lower() == "yes":
        while True:
            inputUN = input("Enter your username: ")
            inputPwd = input("Enter your password: ")
            print("User Login:")

            # Check if the entered username and password match any user in the data
            if any(user_dict['Username'] == inputUN and user_dict['Password'] == inputPwd for user_dict in users_data):
                print("User Login Successful!\n")
                user_menu()
            else:
                print("Invalid login! Please try again.")
    elif main_choice.lower() == "no":
        registration()
    else:
        print("Invalid choice. Please try again.")


def user_menu():
    while True:
        print("\nUser Menu:")
        print("1. Perform Booking")
        print("2. View Booking Information")
        print("3. Delete Their Booking Information")
        print("4. Edit Booking Information")
        print("5. Search Booking Information")
        print("6. Update Profile Information")
        print("7. Logout and Go to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            perform_booking()
        elif choice == '2':
            view_booking()
        elif choice == '3':
            delete_booking()
        elif choice == '4':
            edit_booking()
        elif choice == '5':
            search_booking()
        elif choice == '6':
            update_profile()
        elif choice == '7':
            print("Logging out.")
            main.main()
        else:
            print("Invalid choice. Please try again.")


def perform_booking():
    print("\nPerform Booking Functionality\n")
    # Implement booking functionality here


def view_booking():
    print("\nView Booking Information Functionality\n")
    # Implement viewing booking information functionality here


def delete_booking():
    print("\nDelete Booking Functionality\n")
    # Implement deleting booking functionality here


def edit_booking():
    print("\nEdit Booking Information Functionality\n")
    # Implement editing booking information functionality here


def search_booking():
    print("\nSearch Booking Information Functionality\n")
    # Implement searching booking information functionality here


def update_profile():
    print("\nUpdate Profile Information Functionality\n")
    # Implement updating profile information functionality here


# Main program
def user_login():
    load_users_data()  # Load existing user data from the file
    while True:
        print("\nMAIN MENU:")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
            user_login()