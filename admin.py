import main
import datetime

hall_data = []
booking_data = []
user_data = []


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


def load_hall_data():
    try:
        with open("hall_data.txt", "r") as file:
            for line in file:
                hall_dict = eval(line)
                hall_data.append(hall_dict)
    except FileNotFoundError:
        pass


def enter_hall_information():
    print("\nEnter Hall Information:")
    hall_id = input("Enter Hall ID: ")
    hall_name = input("Enter Hall Name: ")
    hall_description = input("Enter Hall Description: ")
    hall_pax = input("Enter Hall Pax: ")
    hall_availability = input("Enter Hall Availability (Y/N): ")
    hall_rate_price = input("Enter Rate Price per Day: ")

    hall = {
        'Hall ID': hall_id,
        'Hall Name': hall_name,
        'Hall Description': hall_description,
        'Hall Pax': hall_pax,
        'Hall Availability': hall_availability,
        'Rate Price per Day': hall_rate_price
    }

    hall_data.append(hall)
    print("Hall information added successfully.")
    save_hall_data()
    hall_management()


def view_all_hall_information():
    print("\nView All Hall Information:")
    for hall in hall_data:
        print(f"Hall ID: {hall['Hall ID']}, Hall Name: {hall['Hall Name']}, "
              f"Hall Description: {hall['Hall Description']}, Hall Pax: {hall['Hall Pax']}, "
              f"Hall Availability: {hall['Hall Availability']}, Rate Price per Day: {hall['Rate Price per Day']}")

    hall_management()


def search_hall_information():
    print("\nSearch Hall Information:")
    search_term = input("Enter hall name: ")

    search_results = [hall for hall in hall_data
                      if search_term.lower() in hall['Hall Name'].lower() or
                      search_term.lower() in hall['Hall Description'].lower()]

    if search_results:
        print("Search Results:")
        for hall in search_results:
            print(f"Hall ID: {hall['Hall ID']}, Hall Name: {hall['Hall Name']}, "
                  f"Hall Description: {hall['Hall Description']}, Hall Pax: {hall['Hall Pax']}, "
                  f"Hall Availability: {hall['Hall Availability']}, Rate Price per Day: {hall['Rate Price per Day']}")
    else:
        print(f"No results found for '{search_term}'.")

    hall_management()


def edit_hall_information():
    print("\nEdit Hall Information Functionality")

    view_all_hall_information()

    try:
        hall_id_to_edit = input("Enter the Hall ID you want to edit: ")
        hall = next((h for h in hall_data if h['Hall ID'] == hall_id_to_edit), None)

        if hall:
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
            hall['Rate Price per Day'] = hall_rate_price

            save_hall_data()

            print("Hall edited successfully.")
        else:
            print(f"No hall found with Hall ID: {hall_id_to_edit}.")
    except ValueError:
        print("Invalid input. Please enter a valid Hall ID.")


def delete_hall_information():
    print("\nDelete Hall Functionality")

    view_all_hall_information()

    try:
        hall_id_to_delete = input("Enter the Hall ID you want to delete: ")
        hall = next((h for h in hall_data if h['Hall ID'] == hall_id_to_delete), None)

        if hall:
            hall_data.remove(hall)
            save_hall_data()
            print("Hall deleted successfully.")
        else:
            print(f"No hall found with Hall ID: {hall_id_to_delete}.")
    except ValueError:
        print("Invalid input. Please enter a valid Hall ID.")


def save_hall_data():
    with open("hall_data.txt", "w") as file:
        for hall in hall_data:
            file.write(str(hall) + "\n")


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


def view_all_booking_information():
    print("\nView All Booking Information:")
    for booking in booking_data:
        print(f"Event Name: {booking['Event Name']}, "
              f"Hall ID: {booking['Hall ID']}, "
              f"Date and Time Start: {booking['Date and Time Start']}, "
              f"Date and Time End: {booking['Date and Time End']}, "
              f"Payment Price: {booking['Payment Price']} RM")

    booking_management()


def search_booking_information():
    print("\nSearch Booking Information:")
    search_term = input("Enter username or email to search for bookings: ")

    search_results = [booking for booking in booking_data
                      if search_term.lower() in booking['Username'].lower() or
                      search_term.lower() in booking['Email'].lower()]

    if search_results:
        print(f"Search results for '{search_term}':")
        for index, booking in enumerate(search_results, start=1):
            print(f"{index}. Event Name: {booking['Event Name']}, "
                  f"Date and Time: {booking['Date and Time']}, "
                  f"Payment Price: {booking['Payment Price']} RM")
    else:
        print(f"No bookings found for '{search_term}'.")

    booking_management()


def calculate_payment(hall_id, date_time_start, date_time_end):
    # На основе данных о зале и времени бронирования рассчитайте стоимость бронирования.
    # Это может включать в себя проверку доступности зала, расчет времени бронирования и т. д.
    # В данном примере предполагается, что стоимость зависит от разницы между date_time_end и date_time_start.

    # Пример (замените этот код на ваш вариант расчета):
    rate_price_per_day = next((hall['Rate Price per Day'] for hall in hall_data if hall['Hall ID'] == hall_id), None)
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
        if 0 <= booking_index < len(booking_data):
            booking = booking_data[booking_index]

            event_name = input(f"Current Event Name: {booking['Event Name']}. Enter new Event Name: ")
            hall_id = input(f"Current Hall ID: {booking['Hall ID']}. Enter new Hall ID: ")
            date_time_start = input(f"Current Date and Time Start: {booking['Date and Time Start']}. "
                                    f"Enter new Date and Time Start (YYYY-MM-DD HH:MM): ")
            date_time_end = input(f"Current Date and Time End: {booking['Date and Time End']}. "
                                  f"Enter new Date and Time End (YYYY-MM-DD HH:MM): ")

            payment_price = calculate_payment(hall_id, date_time_start, date_time_end)

            booking['Event Name'] = event_name
            booking['Hall ID'] = hall_id
            booking['Date and Time Start'] = date_time_start
            booking['Date and Time End'] = date_time_end
            booking['Payment Price'] = payment_price

            save_booking_data()

            print("Booking edited successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def delete_booking_information():
    print("\nDelete Booking Functionality")

    view_all_booking_information()

    try:
        booking_index = int(input("Enter the index of the booking you want to delete: ")) - 1
        if 0 <= booking_index < len(booking_data):
            del booking_data[booking_index]
            save_booking_data()
            print("Booking deleted successfully.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def save_booking_data():
    with open("booking.txt", "w") as file:
        for booking in booking_data:
            file.write(str(booking) + "\n")


def user_management():
    print("User management")
    print("1) View all the user information")
    print("2) Search user information using the first or last name")
    print("3) Edit the user information")
    print("4) Delete the user from login")
    choice = input("Enter your choice: ")
    if choice == '1':
        view_all_user_information()
    elif choice == '2':
        search_user_information()
    elif choice == '3':
        edit_user_information()
    elif choice == '4':
        delete_user_information()
    else:
        print("Invalid choice. Please try again.")
        user_management()


def view_all_user_information():
    print("\nView All User Information:")
    for user in user_data:
        print(f"Username: {user['Username']}, First Name: {user['First Name']}, "
              f"Last Name: {user['Last Name']}, Email: {user['Email']}, "
              f"Role: {user['Role']}, Status: {user['Status']}")

    user_management()


def search_user_information():
    print("\nSearch User Information:")
    search_term = input("Enter first or last name to search for users: ")

    search_results = [user for user in user_data
                      if search_term.lower() in user['First Name'].lower() or
                      search_term.lower() in user['Last Name'].lower()]

    if search_results:
        print(f"Search results for '{search_term}':")
        for index, user in enumerate(search_results, start=1):
            print(f"{index}. Username: {user['Username']}, "
                  f"First Name: {user['First Name']}, Last Name: {user['Last Name']}, "
                  f"Email: {user['Email']}, Role: {user['Role']}, Status: {user['Status']}")
    else:
        print(f"No users found for '{search_term}'.")

    user_management()


def edit_user_information():
    print("\nEdit User Information Functionality")

    view_all_user_information()

    try:
        username_to_edit = input("Enter the username you want to edit: ")
        user = next((u for u in user_data if u['Username'] == username_to_edit), None)

        if user:
            first_name = input(f"Current First Name: {user['First Name']}. Enter new First Name: ")
            last_name = input(f"Current Last Name: {user['Last Name']}. Enter new Last Name: ")
            email = input(f"Current Email: {user['Email']}. Enter new Email: ")
            role = input(f"Current Role: {user['Role']}. Enter new Role: ")
            status = input(f"Current Status: {user['Status']}. Enter new Status: ")

            user['First Name'] = first_name
            user['Last Name'] = last_name
            user['Email'] = email
            user['Role'] = role
            user['Status'] = status

            save_user_data()

            print("User edited successfully.")
        else:
            print(f"No user found with username: {username_to_edit}.")
    except ValueError:
        print("Invalid input. Please enter a valid username.")


def delete_user_information():
    print("\nDelete User Functionality")

    view_all_user_information()

    try:
        username_to_delete = input("Enter the username you want to delete: ")
        user = next((u for u in user_data if u['Username'] == username_to_delete), None)

        if user:
            user_data.remove(user)
            save_user_data()
            print("User deleted successfully.")
        else:
            print(f"No user found with username: {username_to_delete}.")
    except ValueError:
        print("Invalid input. Please enter a valid username.")


def save_user_data():
    with open("user_data.txt", "w") as file:
        for user in user_data:
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

