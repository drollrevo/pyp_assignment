import main
from datetime import datetime

users_data = []
booking_data = []


def load_users_data():
    try:
        with open("users.txt", "r") as file:
            for line in file:
                user_dict = eval(line)
                users_data.append(user_dict)
    except FileNotFoundError:
        pass


def load_booking_data():
    try:
        with open("booking.txt", "r") as file:
            for line in file:
                booking_dict = eval(line)
                booking_data.append(booking_dict)
    except FileNotFoundError:
        pass


def save_users_data():
    with open("users.txt", "w") as file:
        for user_dict in users_data:
            file.write(str(user_dict) + "\n")


def save_booking_data():
    with open("booking.txt", "w") as file:
        for booking_dict in booking_data:
            file.write(str(booking_dict) + "\n")


def registration():
    print("User Registration:")
    username = input("Enter your username: ")

    while any(user_dict['Username'] == username for user_dict in users_data):
        print("Username already exists. Please choose another one.")
        username = input("Enter your username: ")

    password = input("Enter your password: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    dob = input("Enter your date of birth: ")
    contact_number = input("Enter your contact number: ")
    email = input("Enter your email address: ")

    user_dict = {
        'Username': username,
        'Password': password,
        'First Name': first_name,
        'Last Name': last_name,
        'Date of Birth': dob,
        'Contact Number': contact_number,
        'Email': email
    }

    users_data.append(user_dict)
    save_users_data()
    print("Registration successful!")


def login():
    main_choice = input("Do you have an account? (yes/no): ")

    if main_choice.lower() == "yes":
        while True:
            inputUN = input("Enter your username: ")
            inputPwd = input("Enter your password: ")
            print("User Login:")

            if any(user_dict['Username'] == inputUN and user_dict['Password'] == inputPwd for user_dict in users_data):
                print("User Login Successful!")
                user_menu(inputUN)
            else:
                print("Invalid login! Please try again.")
    elif main_choice.lower() == "no":
        registration()
    else:
        print("Invalid choice. Please try again.")
        login()


def calculate_payment(hall_id, date_time_start, date_time_end):
    hall_type = get_hall_type_by_id(hall_id)
    rent_rate = get_rent_rate_by_hall_type(hall_type)

    total_hours = calculate_total_hours(date_time_start, date_time_end)
    print(f"Total Hours: {total_hours}")
    payment_price = rent_rate * total_hours
    print(f"Payment Price: {payment_price}")

    return payment_price


def get_hall_type_by_id(hall_id):
    hall_types = {"1": "Auditorium", "2": "Banquet Hall", "3": "Meeting Room"}
    return hall_types.get(hall_id, "Unknown")


def get_rent_rate_by_hall_type(hall_type):
    rent_rates = {"Auditorium": 300.00, "Banquet Hall": 100.00, "Meeting Room": 50.00}
    return rent_rates.get(hall_type, 0.00)


def calculate_total_hours(date_time_start, date_time_end):
    try:
        rent_datetime_start = datetime.strptime(date_time_start, "%Y-%m-%d %H:%M")
        rent_datetime_end = datetime.strptime(date_time_end, "%Y-%m-%d %H:%M")
        time_difference = rent_datetime_end - rent_datetime_start
        total_hours = time_difference.total_seconds() / 3600

        return max(total_hours, 0)
    except ValueError:
        print("Invalid date and time format. Please enter in the format: YYYY-MM-DD HH:MM")
        return 0


def perform_booking(username):
    print("Perform Booking Functionality")
    event_name = input("Enter event name: ")
    event_description = input("Enter event description: ")

    print("1: Auditorium, 2: Banquet Hall, 3: Meeting Room")
    while True:
        hall_id = input("Enter hall ID: ")
        if hall_id in ["1", "2", "3"]:
            break
        else:
            print("Invalid hall ID. Please enter a valid ID.")

    while True:
        date_time_start = input("Enter date and time of renting start (YYYY-MM-DD HH:MM): ")
        date_time_end = input("Enter date and time of renting end (YYYY-MM-DD HH:MM): ")
        try:
            datetime.strptime(date_time_start, "%Y-%m-%d %H:%M")
            datetime.strptime(date_time_end, "%Y-%m-%d %H:%M")
            break
        except ValueError:
            print("Invalid date and time format. Please enter in the format: YYYY-MM-DD HH:MM")

    payment_price = calculate_payment(hall_id, date_time_start, date_time_end)

    booking = {
        'Username': username,  # Added username to the booking
        'Event Name': event_name,
        'Event Description': event_description,
        'Hall ID': hall_id,
        'Date and Time Start': date_time_start,
        'Date and Time End': date_time_end,
        'Payment Price': payment_price
    }

    booking_data.append(booking)
    save_booking_data()

    print("\nBooking successful!")
    print(f"Event: {event_name}")
    print(f"Hall ID: {hall_id}")
    print(f"Date and Time Start: {date_time_start}")
    print(f"Date and Time End: {date_time_end}")
    print(f"Payment Price: {payment_price} RM\n")


def view_booking(username):
    print("\nView Booking Information Functionality")

    user_bookings = [booking for booking in booking_data if booking['Username'] == username]

    if user_bookings:
        for index, booking in enumerate(user_bookings, start=1):
            print(f"{index}. Event Name: {booking['Event Name']}, "
                  f"Date and Time: {booking['Date and Time Start']} - {booking['Date and Time End']}, "
                  f"Payment Price: {booking['Payment Price']} RM")
    else:
        print("No bookings found for this user.")


def delete_booking(username):
    print("\nDelete Booking Functionality")

    view_booking(username)

    try:
        booking_index = int(input("Enter the index of the booking you want to delete: ")) - 1
        if 0 <= booking_index < len(booking_data):
            if booking_data[booking_index]['Username'] == username:
                del booking_data[booking_index]
                save_booking_data()
                print("Booking deleted successfully.")
            else:
                print("You can only delete your own bookings.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")


def update_payment_price(booking):
    hall_id = booking['Hall ID']
    date_time_start = booking['Date and Time Start']
    date_time_end = booking['Date and Time End']

    hall_type = get_hall_type_by_id(hall_id)
    rent_rate = get_rent_rate_by_hall_type(hall_type)

    total_hours = calculate_total_hours(date_time_start, date_time_end)
    payment_price = rent_rate * total_hours

    booking['Payment Price'] = payment_price
    save_booking_data()

    print(f"Payment Price updated: {payment_price} RM")


def edit_booking(username):
    print("\nEdit Booking Information Functionality")

    view_booking(username)

    try:
        booking_index = int(input("Enter the index of the booking you want to edit: ")) - 1
        if 0 <= booking_index < len(booking_data):
            booking = booking_data[booking_index]

            if booking['Username'] == username:
                event_name = input(f"Current Event Name: {booking['Event Name']}. Enter new Event Name: ")
                event_description = input(f"Current Event Description: {booking['Event Description']}. "
                                          f"Enter new Event Description: ")

                while True:
                    date_time_start = input("Enter new date and time of renting start (YYYY-MM-DD HH:MM): ")
                    date_time_end = input("Enter new date and time of renting end (YYYY-MM-DD HH:MM): ")
                    try:
                        datetime.strptime(date_time_start, "%Y-%m-%d %H:%M")
                        datetime.strptime(date_time_end, "%Y-%m-%d %H:%M")
                        break
                    except ValueError:
                        print("Invalid date and time format. Please enter in the format: YYYY-MM-DD HH:MM")

                booking['Event Name'] = event_name
                booking['Event Description'] = event_description
                booking['Date and Time Start'] = date_time_start
                booking['Date and Time End'] = date_time_end

                update_payment_price(booking)
                print("Booking edited successfully.")
            else:
                print("You can only edit your own bookings.")
        else:
            print("Invalid index. Please enter a valid index.")
    except ValueError:
        print("Invalid input. Please enter a valid index.")



def search_booking(username):
    print("\nSearch Booking Information Functionality")
    search_term = input("Enter event name to search for bookings: ")

    search_results = [booking for booking in booking_data
                      if search_term.lower() in booking['Event Name'].lower() and booking['Username'] == username]

    if search_results:
        print(f"Search results for '{search_term}':")
        for index, booking in enumerate(search_results, start=1):
            print(f"{index}. Event Name: {booking['Event Name']}, "
                  f"Date and Time: {booking['Date and Time Start']} - {booking['Date and Time End']}, "
                  f"Payment Price: {booking['Payment Price']} RM")
    else:
        print(f"No bookings found for '{search_term}'.")


def update_profile(username):
    print("\nUpdate Profile Information Functionality")

    user = next((user for user in users_data if user['Username'] == username), None)

    if user:
        password = input(f"Current Password: {user['Password']}. Enter new Password: ")
        first_name = input(f"Current First Name: {user['First Name']}. Enter new First Name: ")
        last_name = input(f"Current Last Name: {user['Last Name']}. Enter new Last Name: ")
        dob = input(f"Current Date of Birth: {user['Date of Birth']}. Enter new Date of Birth: ")
        contact_number = input(f"Current Contact Number: {user['Contact Number']}. Enter new Contact Number: ")
        email = input(f"Current Email Address: {user['Email']}. Enter new Email Address: ")

        user.update({
            'Password': password,
            'First Name': first_name,
            'Last Name': last_name,
            'Date of Birth': dob,
            'Contact Number': contact_number,
            'Email': email
        })

        save_users_data()
        print("Profile updated successfully.")
    else:
        print("User not found.")


def user_menu(username):
    while True:
        print("User Menu:")
        print("1. Perform Booking")
        print("2. View Booking Information")
        print("3. Delete Their Booking Information")
        print("4. Edit Booking Information")
        print("5. Search Booking Information")
        print("6. Update Profile Information")
        print("7. Logout and Go to Main Menu")

        choice = input("Enter your choice: ")

        if choice == '1':
            perform_booking(username)
        elif choice == '2':
            view_booking(username)
        elif choice == '3':
            delete_booking(username)
        elif choice == '4':
            edit_booking(username)
        elif choice == '5':
            search_booking(username)
        elif choice == '6':
            update_profile(username)
        elif choice == '7':
            print("Logging out.")
            main.main()
        else:
            print("Invalid choice. Please try again.")
            user_menu(username)


# Main program
def user_login():
    load_users_data()
    while True:
        print("MAIN MENU:")
        print("1. Login")
        print("2. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            login()
        elif choice == "2":
            print("Exiting the system.")
            main.main()
            break
        else:
            print("Invalid choice. Please try again.")
            user_login()


if __name__ == "__main__":
    user_login()
