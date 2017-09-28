import os
import time

os.system('cls')

def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')
    print()

def time_cls():
    time.sleep(4)
    os.system('cls')


numbers = {}
menu_choice = 0

print_menu()
while menu_choice != 5:
    menu_choice = int(input("Type in a number (1-5): "))
    if menu_choice == 1:
        print("Telephone Numbers:")
        for x in numbers.keys():
            print("Name: ", x, "\tNumber:", numbers[x])
        print()
        time_cls()
        print_menu()

    elif menu_choice == 2:
        print("Add Name and Number")
        name = input("Name: ")
        phone = input("Number: ")
        numbers[name] = phone
        time_cls()
        print_menu()

    elif menu_choice == 3:
        print("Remove Name and Number")
        name = input("Name: ")

        if name in numbers:
            del numbers[name]
            time_cls()
            print_menu()

        else:
            print(name, "was not found")
            time_cls()
            print_menu()

    elif menu_choice == 4:
        print("Lookup Number")
        name = input("Name: ")

        if name in numbers:
            print("The number is", numbers[name])
            time_cls()
            print_menu()

        else:
            print(name, "was not found")
            time_cls()
            print_menu()

    elif menu_choice != 5:
        time_cls()

print_menu()
