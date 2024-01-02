import admin
import user

def main():
    while True:
        print("Hall Symphony:")
        print("----------------")
        print("1) Login as Admin")
        print("2) Login as User")
        print("3) Exit Program")
        print("----------------")
        choice = input("Enter your choice:")
        if choice == '1':
            admin.admin_login()
        elif choice == '2':
            user.user_login()
        elif choice == '3':
            print("System exited")
            exit()
        else:
            print("Invalid Choice!")
            main()


# start the program
if __name__ == "__main__":
    main()
