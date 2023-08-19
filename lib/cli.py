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
    print(
        "Would you like to:\n"
        + "1:View Activities\n"
        + "2:View Categories\n"
        + "3:View Table"
    )
    menu_options = input("Type 1, 2 , 3, or exit : ")
    if menu_options == 1:
        # view_activities()
        pass
    elif menu_options == 2:
        # view_categories()
        pass
    elif menu_options == 3:
        # view_categories()
        pass
    elif menu_options.lower() == "exit":
        exit()
    else:
        print("Input must be 'y' for yes, 'n' for no, or exit to exit.")
        time.sleep(3)
        clear_terminal()
        main_menu()


def exit():
    print("Are you sure you want to exit?\n")
    exit_y_or_n = input("y/n: ")
    if exit_y_or_n == "y":
        print("Goodbye!")
        time.sleep(1)
        print("\n" * 64)
        pass
    elif exit_y_or_n == "n":
        clear_terminal()
        main_menu()
    else:
        y_n_error()
        clear_terminal()
        exit()


def clear_terminal():
    print("\n" * 64)


def y_n_error():
    print("Input must be 'y' for yes or 'n' for no.")
    time.sleep(2)


if __name__ == "__main__":
    start()
