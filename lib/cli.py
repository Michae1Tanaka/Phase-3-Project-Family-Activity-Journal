from .db.models.activity import Activity
from .db.models.category import Category
from .db.models.photo import Photo
from .db.models.activity_category_association import activity_category
from .helpers.database_utils import Session
import time

session = Session()


def start():
    print("\n" * 64)
    print("Hello and Welcome to your Family Activity Journal!\n")
    time.sleep(1)
    main_menu()


def main_menu():
    print("Main Menu:\n")
    print("Would you like to:\n1:View Activities\n2:View Categories\n3:View Table")
    menu_option = input("Type 1, 2 , 3, or exit : ")
    if menu_option.lower() == "exit":
        exit(main_menu)
    elif menu_option in ["1", "2", "3"]:
        if int(menu_option) == 2:
            # view_categories()
            pass
        elif int(menu_option) == 3:
            # view_table() or view_photos()
            pass
        elif int(menu_option) == 1:
            activities_menu()
    else:
        multi_choice_error()
        main_menu()


def activities_menu():
    clear_terminal()
    print("Activities Menu:\n")
    print(
        "Would you like to:\n1: Update an activity\n2: Delete an activity\n3: View activities?"
    )
    activity_option = input("Type 1, 2, 3, or exit : ")
    if activity_option.lower() == "exit":
        exit(activities_menu)
    elif activity_option in ["1", "2", "3"]:
        activity_option = int(activity_option)
        if activity_option == 2:
            # delete_activity()
            pass
        elif activity_option == 3:
            # update_activity()
            pass
        elif activity_option == 1:
            # view_activities()
            pass
    else:
        multi_choice_error()
        activities_menu()


def exit(prev_menu):
    print("Are you sure you want to exit?\n")
    exit_y_or_n = input("y/n: ")
    if exit_y_or_n == "y":
        print("Goodbye!")
        time.sleep(1)
        print("\n" * 64)
        pass
    elif exit_y_or_n == "n":
        clear_terminal()
        prev_menu()
    else:
        y_n_error()
        clear_terminal()
        exit()


def clear_terminal():
    print("\n" * 64)


def multi_choice_error():
    clear_terminal()
    print("Input must be a number that corresponds to an option or exit.")
    time.sleep(3)
    clear_terminal()


def y_n_error():
    clear_terminal()
    print("Input must be 'y' for yes or 'n' for no.")
    time.sleep(2)
    clear_terminal()


if __name__ == "__main__":
    start()
