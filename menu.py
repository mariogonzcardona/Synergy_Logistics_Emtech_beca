from processes import *
# Menu interactivo por consola 

# Preparacion de metodos para login y register
def register(user_email,password):
    return True

def login(user_email,password):
    return True

def show_login_register_menu():
    while True:
        print("-"*50)
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        print("-"*50)
        try:
            option = int(input("Select an option: "))
            if option == 1:
                user_email = input("Enter your email: ")
                password = input("Enter your password: ")
                if login(user_email,password):
                    print("Login successful")
                    show_options_menu()
                else:
                    print("Login failed")
            elif option == 2:
                user_email = input("Enter your email: ")
                password = input("Enter your password: ")
                if register(user_email,password):
                    print("Register successful please login")
                else:
                    print("Register failed")
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
            
def show_options_menu():
    while True:
        print("-"*50)
        print("1. Show Most demanded Import and Export Routes")
        print("2. Show Most demanded types of transport for Import and Export")
        print("3. Show Countries that generate 80% of the value of exports and imports")
        print("4. Exit")
        print("-"*50)
        try:
            option = int(input("Select an option: "))
            if option == 1:
                show_process_report_1()
            elif option == 2:
                show_process_report_2()
            elif option == 3:
                show_process_report_3()
            elif option == 4:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")

def show_process_report_1():
    while True:
        print("-"*50)
        print("1. Show the 10 most demanded routes for Import")
        print("2. Show the 10 most demanded routes for Export")
        print("3. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                option_1(1)
            elif option == 2:
                option_1(2)
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
            
def show_process_report_2():
    while True:
        print("-"*50)
        print("1. Show the most demanded transports for Imports")
        print("2. Show the most demanded transports for Exports")
        print("3. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                option_2(1)
            elif option == 2:
                option_2(2)
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")
            
def show_process_report_3():
    while True:
        print("-"*50)
        print("1. Show the Countries that generate 80% of the value of imports")
        print("2. Show the Countries that generate 80% of the value of exports")
        print("3. Exit")
        try:
            option = int(input("Select an option: "))
            if option == 1:
                option_3(1)
            elif option == 2:
                option_3(2)
            elif option == 3:
                break
            else:
                print("Invalid option")
        except ValueError:
            print("Invalid option")