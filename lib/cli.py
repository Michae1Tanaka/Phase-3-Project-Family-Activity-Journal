from .db.models.activity import Activity
from .db.models.category import Category
from .db.models.photo import Photo
from .db.models.activity_category_association import activity_category
from .helpers.database_utils import Session
import time

session = Session()
current_page = None
last_page = None


def start():
    print("\n" * 64)
    print("Hello and Welcome to your Family Activity Journal!\n")
    time.sleep(1)
    main_menu()


def main_menu():
    global current_page
    current_page = main_menu
    print("Main Menu:\n")
    print("Would you like to:\n1:View Activities\n2:View Categories\n3:View Table")
    menu_option = input("Type 1, 2 , 3, or exit: ")
    if menu_option.lower() == "exit":
        clear_terminal()
        exit()
    elif menu_option in ["1", "2", "3"]:
        global last_page
        last_page = main_menu
        if int(menu_option) == 1:
            activities_menu()
        elif int(menu_option) == 2:
            categories_menu()
            pass
        elif int(menu_option) == 3:
            # view_table() or view_photos()
            pass
    else:
        multi_choice_error()
        main_menu()


def activities_menu():
    global current_page
    current_page = activities_menu
    clear_terminal()
    print("Activities Menu:\n")
    print(
        "Would you like to:\n1: Create an activity\n2: Update an activity\n3: Delete an activity?"
    )
    activity_option = input("Type 1, 2, 3, exit, or back : ")
    if activity_option.lower() == "exit":
        clear_terminal()
        exit()
    elif activity_option.lower() == "back":
        clear_terminal()
        back()
    elif activity_option in ["1", "2", "3"]:
        global last_page
        last_page = activities_menu
        activity_option = int(activity_option)
        if activity_option == 1:
            # create_activity()
            pass
        elif activity_option == 2:
            # update_activity()
            pass
        elif activity_option == 3:
            # delete_activity()
            pass
    else:
        multi_choice_error()
        activities_menu()


def categories_menu():
    global current_page
    current_page = categories_menu
    clear_terminal()
    print("Categories Menu\n")
    print(
        "Would you like to:\n1:Create a category\n2:Update a category\n3:Delete a category"
    )
    category_option = input("Type 1, 2, 3, exit, or back : ")
    if category_option.lower() == "exit":
        clear_terminal()
        exit()
    if category_option.lower() == "back":
        clear_terminal()
        back()
    elif category_option in ["1", "2", "3"]:
        category_option = int(category_option)
        if category_option == "1":
            # create_category
            pass
        elif category_option == "2":
            # update_category
            pass
        elif category_option == "3":
            # delete_category
            pass
    else:
        multi_choice_error()
        categories_menu()


def exit():
    print("Are you sure you want to exit?\n")
    exit_y_or_n = input("y/n: ")
    if exit_y_or_n.lower() == "y":
        print("Goodbye!")
        time.sleep(1)
        clear_terminal()
    elif exit_y_or_n.lower() == "n":
        clear_terminal()
        if current_page:
            current_page()
        else:
            main_menu()
    else:
        y_n_error()
        clear_terminal()


def clear_terminal():
    print("\n" * 64)


def multi_choice_error():
    clear_terminal()
    print("Input must be a number that corresponds to an option,  exit, or back.")
    time.sleep(3)
    clear_terminal()


def back():
    last_page()


def y_n_error():
    clear_terminal()
    print("Input must be 'y' for yes or 'n' for no.")
    time.sleep(2)
    clear_terminal()
    exit()


if __name__ == "__main__":
    start()
