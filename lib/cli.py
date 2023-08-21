from .db.models.activity import Activity
from .db.models.category import Category
from .db.models.photo import Photo
from .db.models.activity_category_association import activity_category
from .helpers.database_utils import Session
import time
from prettytable import PrettyTable
import os
from datetime import date

table = PrettyTable()
session = Session()
current_page = None
width = os.get_terminal_size().columns


def start():
    clear_terminal()
    print("Hello and Welcome to your Family Activity Journal!\n")
    time.sleep(1)
    main_menu()


def main_menu():
    global current_page
    current_page = main_menu
    clear_terminal()
    print("Main Menu:\n")
    print("Would you like to:\n1:View Activities\n2:View Categories\n3:View Table")
    menu_option = input("Type 1, 2 , 3, or exit: ").strip()
    if menu_option.lower() == "exit":
        clear_terminal()
        exit()
    elif menu_option in ["1", "2", "3"]:
        if menu_option == "1":
            activities_menu()
        elif menu_option == "2":
            categories_menu()
            pass
        elif menu_option == "3":
            # photos menu
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
        "Would you like to:\n1: View activities?\n2: Create an activity?\n3: Update an activity?\n4: Delete an activity?"
    )
    activity_option = input("Type 1, 2, 3, 4, exit, or back : ").strip()
    if activity_option.lower() == "exit":
        clear_terminal()
        exit()
    elif activity_option.lower() == "back":
        clear_terminal()
        main_menu()
    elif activity_option in ["1", "2", "3", "4"]:
        if activity_option == "1":
            view_activities()
        elif activity_option == "2":
            create_activity()
            pass
        elif activity_option == "3":
            # add photo?
            pass
        elif activity_option == "4":
            #
            pass
    else:
        multi_choice_error()
        activities_menu()


def view_activities():
    global current_page
    current_page = view_activities
    start = 0
    end = 10
    total_amount_of_activities = len(Activity.get_all_activities(session))

    display_table(start, end)

    loop = True
    while loop:
        if end >= total_amount_of_activities:
            user_input_table = input(
                "Type 'p' for previous, an ID to view, update, or delete an activity, 'back', or 'exit': "
            ).strip()
        elif start == 0:
            user_input_table = input(
                "Type 'n' for next to see the next 10 activities, an ID to view, update, or delete an activity, 'back', or 'exit': "
            ).strip()
        else:
            user_input_table = input(
                "Type 'n' for next to see the next 10 activities, 'p' for previous to see previous 10, an ID to view, update, or delete an activity, 'back', or 'exit': "
            ).strip()

        if user_input_table.isdigit():
            chosen_id = int(user_input_table)
            activity = session.query(Activity).all()[chosen_id]
            if activity:
                loop = False
                update_activity_prompt(chosen_id)
            else:
                clear_terminal()
                print("No activity found with the specified ID.")
                display_table(start, end)
        elif user_input_table.lower() == "n" and end < total_amount_of_activities:
            start += 10
            end += 10
            if end > total_amount_of_activities:
                end = total_amount_of_activities
            display_table(start, end)
        elif user_input_table.lower() == "p" and start > 0:
            start -= 10
            end = start + 10
            display_table(start, end)
        elif user_input_table.lower() == "back":
            loop = False
            clear_terminal()
            activities_menu()
        elif user_input_table.lower() == "exit":
            clear_terminal()
            loop = False
            exit()
        else:
            clear_terminal()
            multi_choice_error()
            display_table(start, end)


def create_activity():
    clear_terminal()
    print("Create Activity Menu".center(width))
    activity_instance = dict()
    activity_name = input("Input activity name: ").strip()
    if 0 < len(activity_name) <= 68:
        activity_instance["name"] = activity_name
        activity_description = input("Input activity description: ").strip()
        if 0 < len(activity_description) <= 68:
            activity_instance["description"] = activity_description
            activity_notes = input("Input activity note: ").strip()
            if 0 < len(activity_notes) <= 68:
                activity_instance["notes"] = activity_notes
                activity_location = input(
                    "Input activity location (City,State or City, Region, Country):  "
                ).strip()
                if 0 < len(activity_location) and 0 < activity_location.count(",") <= 2:
                    activity_instance["location"] = activity_location
                    activity_weather = (
                        input(
                            'Input activity weather condition ["Clear", "Cloudy", "Rainy", "Snowy", "Windy", "Foggy", "Hot", "Cold", "Mild", "Sunny"]: '
                        )
                        .strip()
                        .title()
                    )
                    if activity_weather in (
                        "Clear",
                        "Cloudy",
                        "Rainy",
                        "Snowy",
                        "Windy",
                        "Foggy",
                        "Hot",
                        "Cold",
                        "Mild",
                        "Sunny",
                    ):
                        activity_instance["weather"] = activity_weather
                        activity_date = input(
                            "Input activity date (YYYY-MM-DD): "
                        ).strip()
                        if is_valid_date(activity_date):
                            activity_instance["date"] = activity_date
                            clear_terminal()
                            print("Does this activity information look correct?")
                            print("Activity name: " + activity_instance["name"])
                            print(
                                "Activity description: "
                                + activity_instance["description"]
                            )
                            print("Activity note: " + activity_instance["notes"])
                            print("Activity location: " + activity_instance["location"])
                            print("Activity weather: " + activity_instance["weather"])
                            print("Activity date: " + activity_instance["date"])
                            confirmation = input("y/n : ").strip()
                            if confirmation == "y":
                                new_activity = Activity.add_activity(
                                    name=activity_instance["name"],
                                    description=activity_instance["description"],
                                    notes=activity_instance["notes"],
                                    location=activity_instance["location"],
                                    weather=activity_instance["weather"],
                                    date=activity_instance["date"],
                                )
                                session.add(new_activity)
                                session.commit()
                                print("Activity has been added to the table!")
                                time.sleep(3)
                                main_menu()
                            elif confirmation == "n":
                                clear_terminal()
                                print("Activity was not saved.")
                                time.sleep(3)
                                activities_menu()
                            else:
                                clear_terminal()
                                y_n_error()
                                create_activity()
                        else:
                            clear_terminal()
                            print(
                                "The activity date must be in the format of YYYY-MM-DD"
                            )
                            time.sleep(3)
                            create_activity()
                    else:
                        clear_terminal()
                        print(
                            "The weather must be either 'Clear, 'Cloudy', 'Rainy', 'Snowy','Windy','Foggy','Hot','Cold','Mild', or 'Sunny'."
                        )
                        time.sleep(3)
                        create_activity()
                else:
                    clear_terminal()
                    print(
                        "The location must be in the format 'City,State' or 'City,Region,Country"
                    )
                    time.sleep(3)
                    create_activity()
            else:
                clear_terminal()
                print("The activity note must be in between 0 and 69 characters.")
                time.sleep(3)
                create_activity()
        else:
            clear_terminal()
            print("The activity description must be between 0 and 69 characters.")
            time.sleep(3)
            create_activity()
    else:
        clear_terminal()
        print("The activity name must be between 0 and 69 characters.")
        time.sleep(3)
        create_activity()


def update_activity_prompt(chosen_id):
    global current_page
    current_page = view_activities
    activity = session.query(Activity).all()[chosen_id - 1]
    clear_terminal()
    print(f"You have selected: \n\n{activity}")
    correct_yn = input("y/n : ").strip()
    if correct_yn == "y":
        clear_terminal()
        print(f"Updating activity: \n\n{activity}")

        new_name = input("Enter new name or press enter to skip: ").strip()
        if new_name:
            activity.name = new_name

        new_description = input(
            "Enter new description or press enter to skip: "
        ).strip()
        if new_description:
            activity.description = new_description

        new_note = input("Enter new note or press enter to skip: ").strip()
        if new_note:
            activity.notes = new_note

        new_location = input("Enter new location or press enter to skip: ").strip()
        if new_location:
            activity.location = new_location

        new_weather = input(
            "Enter new weather condition ['Clear', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Foggy', 'Hot', 'Cold', 'Mild', or 'Sunny'] or press enter to skip: "
        ).strip()
        if new_weather:
            activity.weather = new_weather

        new_date = input("Enter new date or press enter to skip: ").strip()
        if new_date:
            activity.date = new_date
        print(activity)
        print("Would you like to update this activity?")
        update_yn = input("y/n: ").strip()
        if update_yn == "y":
            session.commit()
            print("Activity updated successfully!")
            main_menu()
        else:
            clear_terminal()
            y_n_error()
    elif correct_yn == "n":
        view_activities()
    else:
        print("Activity with specified ID not found.")


def categories_menu():
    global current_page
    current_page = categories_menu
    clear_terminal()
    print("Categories Menu\n")
    print(
        "Would you like to:\n1:Create a category\n2:Update a category\n3:Delete a category"
    )
    category_option = input("Type 1, 2, 3, exit, or back : ").strip()
    if category_option.lower() == "exit":
        clear_terminal()
        exit()
    elif category_option.lower() == "back":
        clear_terminal()
        main_menu()
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


def display_table(start, end):
    activities = Activity.get_all_activities(session)
    activity_ids = [activity.id for activity in activities[start:end]]
    activity_names = [activity.name for activity in activities[start:end]]
    activity_weather = [activity.weather for activity in activities[start:end]]
    activity_notes = [activity.notes for activity in activities[start:end]]
    activity_locations = [activity.location for activity in activities[start:end]]
    activity_dates = [
        f"{activity.date.month}-{activity.date.day}-{activity.date.year}"
        for activity in activities[start:end]
    ]

    table = PrettyTable()
    table.field_names = ["ID", "Activity", "Location", "Weather", "Notes", "Date"]

    for id, activity, location, weather, notes, date in zip(
        activity_ids,
        activity_names,
        activity_locations,
        activity_weather,
        activity_notes,
        activity_dates,
    ):
        table.add_row([id, activity, location, weather, notes, date])

    clear_terminal()
    width = os.get_terminal_size().columns
    print("Activities Table".center(width))
    print(table)


def exit():
    print("Are you sure you want to exit?\n")
    exit_y_or_n = input("y/n: ").strip()
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
    print("Input must correspond to an option.")
    time.sleep(3)
    clear_terminal()


def y_n_error():
    clear_terminal()
    print("Input must be 'y' for yes or 'n' for no.")
    time.sleep(2)
    clear_terminal()
    exit()


def is_valid_date(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    start()
