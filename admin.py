import main
import user
import datetime
from datetime import datetime

halls_data = []
booking_data = []
users_data = []


def admin_login():
    while True:
        inputUN = input("Enter your admin name:")
        inputPwd = input("Enter you password:")
        print("Admin Login:")
        if inputUN == "admin" and inputPwd == "123":
            admin_menu()
        else:
            print("Invalid login!")
            admin_login()


def hall_management():
    print("Hall Management")
    print("1. Enter Hall Information")
    print("2. View All Hall Information")
    print("3. Search Hall Information")
    print("4. Edit Hall Information")
    print("5. Delete Hall Information")
    print("6. Go Back to Admin Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        enter_hall_information()
    elif choice == '2':
        view_all_hall_information()
    elif choice == '3':
        search_hall_information()
    elif choice == '4':
        edit_hall_information()
    elif choice == '5':
        delete_hall_information()
    elif choice == '6':
        admin_menu()
    else:
        print("Invalid choice. Please try again.")
        hall_management()


def save_hall_data(halls_data):
    with open("halls.txt", "a") as file:
        for hall in halls_data:
            file.write(str(hall) + "\n")


def save_hall_data_danger(halls_data):
    with open("halls.txt", "w") as file:
        for hall in halls_data:
            file.write(str(hall) + "\n")


def enter_hall_information():
    print("Enter Hall Information:")

    hall_id = input("Enter Hall ID: ")

    # Check if the hall ID already exists
    while any(hall['Hall ID'] == hall_id for hall in halls_data):
        print("Hall ID already exists. Please choose another one.")
        hall_id = input("Enter Hall ID: ")

    hall_name = input("Enter Hall Name: ")
    hall_description = input("Enter Hall Description: ")
    hall_pax = input("Enter Hall Pax: ")
    hall_availability = input("Enter Hall Availability: ")
    hall_rate = input("Enter Rate Price per Day: ")

    new_hall = {
        'Hall ID': hall_id,
        'Hall Name': hall_name,
        'Hall Description': hall_description,
        'Hall Pax': hall_pax,
        'Hall Availability': hall_availability,
        'Rate Price per Day': f'{float(hall_rate):.2f}'  # Convert rate to float and format as string
    }

    halls_data.append(new_hall)
    save_hall_data(halls_data)

    print(f"Hall {hall_name} added successfully!\n")
    hall_management()


def view_all_hall_information():
    halls_data = user.load_hall_type()
    print("\nView All Hall Information:")
    for hall_info in halls_data:
        print(f"Hall ID: {hall_info['Hall ID']}, "
              f"Hall Name: {hall_info['Hall Name']}, "
              f"Hall Description: {hall_info['Hall Description']}, "
              f"Hall Pax: {hall_info['Hall Pax']}, "
              f"Hall Availability: {hall_info['Hall Availability']}, "
              f"Rate Price per Day: {hall_info['Rate Price per Day']}")


def search_hall_information():
    halls_data = user.load_hall_type()  # Load hall data only once
    print("\nSearch Hall Information:")
    search_term = input("Enter hall name: ")

    search_results = [hall_info for hall_info in halls_data
                      if search_term.lower() in hall_info['Hall Name'].lower()]

    if search_results:
        for hall_info in search_results:
            print(f"Hall ID: {hall_info['Hall ID']}, "
                  f"Hall Name: {hall_info['Hall Name']}, "
                  f"Hall Description: {hall_info['Hall Description']}, "
                  f"Hall Pax: {hall_info['Hall Pax']}, "
                  f"Hall Availability: {hall_info['Hall Availability']}, "
                  f"Rate Price per Day: {hall_info['Rate Price per Day']}")
    else:
        print(f"No results found for '{search_term}'.")
    hall_management()


def edit_hall_information():
    halls_data = user.load_hall_type()
    print("\nEdit Hall Information Functionality")

    view_all_hall_information()
    try:
        hall_id_to_edit = input("Enter the Hall ID you want to edit: ")
        hall = next((h for h in halls_data if h['Hall ID'] == hall_id_to_edit), None)

        if hall:
            print(f"Editing Hall ID: {hall['Hall ID']}")

            # Add a check if the hall can be edited (you can customize this condition)
            # For example, check if the hall is not currently booked

            hall_name = input(f"Current Hall Name: {hall['Hall Name']}. Enter new Hall Name: ")
            hall_description = input(
                f"Current Hall Description: {hall['Hall Description']}. Enter new Hall Description: ")
            hall_pax = input(f"Current Hall Pax: {hall['Hall Pax']}. Enter new Hall Pax: ")
            hall_availability = input(
                f"Current Hall Availability: {hall['Hall Availability']}. Enter new Hall Availability (Y/N): ")
            hall_rate_price = input(
                f"Current Rate Price per Day: {hall['Rate Price per Day']}. Enter new Rate Price per Day: ")

            hall['Hall Name'] = hall_name
            hall['Hall Description'] = hall_description
            hall['Hall Pax'] = hall_pax
            hall['Hall Availability'] = hall_availability
            hall['Rate Price per Day'] = float(hall_rate_price)  # Convert rate to float

            save_hall_data_danger(halls_data)

            print("Hall edited successfully.")
        else:
            print(f"No hall found with Hall ID: {hall_id_to_edit}.")
    except ValueError:
        print("Invalid input. Please enter a valid Hall ID.")
    hall_management()


def delete_hall_information():
    print("\nDelete Hall Functionality")

    halls_data = user.load_hall_type()
    view_all_hall_information()

    try:
        hall_id_to_delete = input("Enter the Hall ID you want to delete: ")
        hall = next((h for h in halls_data if h['Hall ID'] == hall_id_to_delete), None)

        if hall:
            halls_data.remove(hall)
            save_hall_data_danger(halls_data)
            print("Hall deleted successfully.")
        else:
            print(f"No hall found with Hall ID: {hall_id_to_delete}.")
    except ValueError:
        print("Invalid input. Please enter a valid Hall ID.")

    hall_management()


def booking_management():
    print("Booking Management")
    print("1. View All Booking Information")
    print("2. Search Booking Information")
    print("3. Edit Booking Information")
    print("4. Delete/Cancel Booking Information")
    print("5. Go Back to Admin Menu")

    choice = input("Enter your choice: ")

    if choice == '1':
        view_all_booking_information()
    elif choice == '2':
        search_booking_information()
    elif choice == '3':
        edit_booking_information()
    elif choice == '4':
        delete_booking_information()
    elif choice == '5':
        admin_menu()
    else:
        print("Invalid choice. Please try again.")
        booking_management()


def load_booking_data():
    try:
        with open("booking.txt", "r") as file:
            booking_data = [eval(line.strip()) for line in file]
        return booking_data
    except Exception as e:
        print(f"Error loading booking data: {e}")
        return []


def view_all_booking_information():
    booking_data = load_booking_data()

    if booking_data:
        print("\nView All Booking Information:")
        for index, booking in enumerate(booking_data, start=1):
            print(f"{index}. Username: {booking.get('Username', 'N/A')}, "
                  f"Event Name: {booking.get('Event Name', 'N/A')}, "
                  f"Hall ID: {booking.get('Hall ID', 'N/A')}, "
                  f"Date and Time Start: {booking.get('Date and Time Start', 'N/A')}, "
                  f"Date and Time End: {booking.get('Date and Time End', 'N/A')}, "
                  f"Payment Price: {booking.get('Payment Price', 'N/A')} RM")
    else:
        print("Error loading booking data.")


def search_booking_information():
    booking_data = load_booking_data()
    print("\nSearch Booking Information:")
    search_term = input("Enter username to search for bookings: ")

    search_results = [booking for booking in booking_data
                      if 'Username' in booking and search_term.lower() in booking['Username'].lower()]

    if search_results:
        print(f"Search results for '{search_term}':")
        for index, booking in enumerate(search_results, start=1):
            print(f"{index}. Event Name: {booking.get('Event Name', 'N/A')}, "
                  f"Date and Time: {booking.get('Date and Time', 'N/A')}, "
                  f"Payment Price: {booking.get('Payment Price', 'N/A')} RM")
    else:
        print(f"No bookings found for '{search_term}'.")

    booking_management()


def calculate_payment(hall_id, date_time_start, date_time_end):
    rate_price_per_day = next((hall['price'] for hall in halls_data if hall['id'] == hall_id), None)
    if rate_price_per_day is not None:
        try:
            date_time_start = datetime.datetime.strptime(date_time_start, "%Y-%m-%d %H:%M")
            date_time_end = datetime.datetime.strptime(date_time_end, "%Y-%m-%d %H:%M")
            duration = (date_time_end - date_time_start).days
            payment_price = int(rate_price_per_day) * duration
            return payment_price
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD HH:MM.")
    return None


def edit_booking_information():
    print("\nEdit Booking Information Functionality")

    view_all_booking_information()

    try:
        booking_index = int(input("Enter the index of the booking you want to edit: ")) - 1
        booking_data = load_booking_data()

        if 0 <= booking_index < len(booking_data):
            booking = booking_data[booking_index]

            cur_username = input(f"Current Username: {booking.get('Username', 'N/A')}. Enter new Username: ")
            event_name = input(f"Current Event Name: {booking.get('Event Name', 'N/A')}. Enter new Event Name: ")
            cur_desc = input(f"Current Desc: {booking.get('Event Description', 'N/A')}. Enter new Event Description: ")
            hall_id = input(f"Current Hall ID: {booking.get('Hall ID', 'N/A')}. Enter new Hall ID: ")

            while True:
                date_time_start = input("Enter new date and time of renting start (YYYY-MM-DD HH:MM): ")
                date_time_end = input("Enter new date and time of renting end (YYYY-MM-DD HH:MM): ")
                try:
                    datetime.strptime(date_time_start, "%Y-%m-%d %H:%M")
                    datetime.strptime(date_time_end, "%Y-%m-%d %H:%M")
                    break
                except ValueError:
                    print("Invalid date and time format. Please enter in the format: YYYY-MM-DD HH:MM")
            del booking_data[booking_index]
            payment_price = user.calculate_payment(hall_id, date_time_start, date_time_end)

            booking_dict = {
                'Username': cur_username,
                'Event Name': event_name,
                'Event Description': cur_desc,
                'Hall ID': hall_id,
                'Date and Time Start': date_time_start,
                'Date and Time End': date_time_end,
                'Payment Price': payment_price
            }
            booking_data.append(booking_dict)
            print(booking_data)
            save_booking_data1(booking_data)

            print("Booking edited successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

    booking_management()


# def save_booking_data1(bookings, filename='booking.txt'):
#     try:
#         with open(filename, 'w') as file:
#             for booking in bookings:
#                 file.write(str(booking) + '\n')
#         print("Booking data saved successfully.")
#     except Exception as e:
#         print(f"Error saving booking data: {e}")
def save_booking_data1(booking_data):
    with open("booking.txt", "w") as file:
        for booking_dict in booking_data:
            file.write(str(booking_dict) + "\n")

def delete_booking_information():
    print("\nDelete Booking Functionality")

    view_all_booking_information()
    booking_data = load_booking_data()
    try:
        booking_index = int(input("Enter the index of the booking you want to delete: ")) - 1
        if 0 <= booking_index < len(booking_data):
            del booking_data[booking_index]
            save_booking_data1(booking_data)
            print("Booking deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")
    booking_management()



def save_booking_data():
    with open("booking.txt", "a") as file:
        for booking in booking_data:
            file.write(str(booking) + "\n")


def user_management():
    print("User management")
    print("1) View all the user information")
    print("2) Search user information using username")
    print("3) Edit the user information")
    print("4) Delete the user from login")
    print("5) Admin menu")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_all_user_information()
    elif choice == '2':
        search_user_information()
    elif choice == '3':
        edit_user_information()
    elif choice == '4':
        delete_user_information()
    elif choice == '5':
        admin_menu()
    else:
        print("Invalid choice. Please try again.")
        user_management()

def load_users_data():
    try:
        with open("users.txt", "r") as file:
            users_data = [eval(line.strip()) for line in file]
        return users_data
    except FileNotFoundError:
        pass

def view_all_user_information():
    print("\nView All User Information:")
    users_data = load_users_data()
    for index, user in enumerate(users_data, start=1):
        print(f"{index}. Username: {user.get('Username', 'N/A')}, "
              f"Password: {user.get('Password', 'N/A')}, "
              f"First Name: {user.get('First Name', 'N/A')}, "
              f"Last Name: {user.get('Last Name', 'N/A')}, "
              f"Date of Birth: {user.get('Date of Birth', 'N/A')}, "
              f"Contact Number: {user.get('Contact Number', 'N/A')}, "
              f"Email: {user.get('Email', 'N/A')}, ")



def search_user_information():
    print("\nSearch User Information:")
    search_term = input("Enter Username to search for users: ")
    users_data = load_users_data()
    search_results = [user for user in users_data
                      if search_term.lower() in user.get('Username', '').lower()]

    if search_results:
        print(f"Search results for '{search_term}':")
        for index, user in enumerate(search_results, start=1):
            print(f"{index}. Username: {user.get('Username', 'N/A')}, "
                  f"First Name: {user.get('First Name', 'N/A')}, Last Name: {user.get('Last Name', 'N/A')}, "
                  f"Email: {user.get('Email', 'N/A')},")
    else:
        print(f"No users found for '{search_term}'.")

    user_management()



def edit_user_information():
    print("\nEdit User Information Functionality")

    view_all_user_information()

    try:
        username_index = int(input("Enter the index of user you want to edit: ")) - 1
        users_data = load_users_data()

        if 0 <= username_index < len(users_data):
            user = users_data[username_index]

            username = input(f"Current Username: {user.get('Username', 'N/A')}. Enter new Username: ")
            password = input(f"Current Password: {user.get('Password', 'N/A')}. Enter new Password: ")
            first_name = input(f"Current First Name: {user.get('First Name', 'N/A')}. Enter new First Name: ")
            last_name = input(f"Current Last Name: {user.get('Last Name', 'N/A')}. Enter new Last Name: ")
            db = input(f"Current Date of Birth: {user.get('Date of Birth', 'N/A')}. Enter new Date of Birth: ")
            cn = input(f"Current Contact Number: {user.get('Contact Number', 'N/A')}. Enter new Contact Number: ")
            email = input(f"Current Email: {user.get('Email', 'N/A')}. Enter new Email: ")
            del users_data[username_index]
            updated_user = {
                'Username': username,
                'Password': password,
                'First Name': first_name,
                'Last Name': last_name,
                'Date of Birth': db,
                'Contact Number': cn,
                'Email': email
            }

            users_data.append(updated_user)
            save_user_data1(users_data)

            print("User edited successfully.")
        else:
            print(f"No user found with this index")
    except ValueError:
        print("Invalid input. Please enter a valid index.")

def save_user_data1(users_data):
    with open("users.txt", "w") as file:
        for user in users_data:
            file.write(str(user) + "\n")

def delete_user_information():
    print("\nDelete User Functionality")

    view_all_user_information()
    users_data = load_users_data()
    try:
        user_index = int(input("Enter the index of the user you want to delete: ")) - 1
        if 0 <= user_index < len(users_data):
            del users_data[user_index]
            save_user_data1(users_data)
            print("User deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")




def save_user_data():
    with open("user_data.txt", "w") as file:
        for user in users_data:
            file.write(str(user) + "\n")


def admin_menu():
    while True:
        print("Admin Menu:")
        print("----------------")
        print("1) Hall Management")
        print("2) Booking Management")
        print("3) User Management")
        print("4) Logout")
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
            print("Invalid choice. Please try again.")
            admin_menu()


if __name__ == "__main__":
    main.main()
