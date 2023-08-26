from .db.models.activity import Activity
from .db.models.category import Category
from .db.models.photo import Photo
from .db.models.activity_category_association import activity_category
from .helpers.database_utils import Session
import time
from prettytable import PrettyTable
from datetime import date
import os


session = Session()
last_page = None
width = os.get_terminal_size().columns


def start():
    clear_terminal()
    print("Hello and Welcome to your Family Activity Journal!\n".center(width))
    time.sleep(3)
    main_menu()


def main_menu():
    global last_page
    last_page = main_menu
    clear_terminal()
    print("Welcome to the Main Menu!".center(width))
    print(
        "\nSelect an option:\n\n1: Access Activity Menu\n2: Access Category Menu\n3: Access Photo Menu\n"
    )
    menu_option = input("Enter 1, 2, 3, or type 'exit' to quit: ").strip()

    if menu_option.lower() == "exit":
        exit()
    elif menu_option in ["1", "2", "3"]:
        if menu_option == "1":
            activities_menu()
        elif menu_option == "2":
            categories_menu()
        elif menu_option == "3":
            photo_menu()
    else:
        multi_choice_error()
        main_menu()


def activities_menu():
    global last_page
    last_page = activities_menu
    clear_terminal()
    print("Activity Menu".center(width))
    print(
        "\nWhat would you like to do?\n\n1: View existing activities\n2: Create a new activity\n3: Filter activities by category\n"
    )
    activity_option = input(
        "Enter 1, 2, 3, 'exit' to quit, or 'back' to return to the main menu: "
    ).strip()
    if activity_option.lower() == "exit":
        exit()
    elif activity_option.lower() == "back":
        main_menu()
    elif activity_option in ["1", "2", "3"]:
        if activity_option == "1":
            view_activities()
        elif activity_option == "2":
            create_activity()
        elif activity_option == "3":
            view_activities_based_on_category()
    else:
        multi_choice_error()
        activities_menu()


def view_activities():
    global last_page
    last_page = view_activities
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
            chosen_id = int(user_input_table) - 1
            activity = session.query(Activity).all()[chosen_id]
            loop = False
            if activity:
                loop = False
                chosen_activity(chosen_id)
            else:
                clear_terminal()
                loop = False
                print("No activity found with the specified ID.")
                view_activities()
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
            activities_menu()
        elif user_input_table.lower() == "exit":
            loop = False
            exit()
        else:
            multi_choice_error()
            loop = False
            display_table(start, end)


def chosen_activity(chosen_id):
    global last_page
    last_page = view_activities
    activity = session.query(Activity).all()[chosen_id]
    clear_terminal()
    print(f"You have selected the following activity:\n\n{activity}\n\n")
    correct_yn = input("Is this the activity you were looking for? (y/n): ").strip()
    if correct_yn == "y":
        clear_terminal()
        print(
            "Would you like to View, Update, or Delete the Activity\n\n\n\n".center(
                width
            )
        )
        view_update_delete = input(
            "Type 'v' to view, 'u' to update, 'd' to delete, or 'a' to attach a photo or category to the activity: "
        ).strip()
        if view_update_delete.lower() == "v":
            view_activity(chosen_id)
        elif view_update_delete.lower() == "u":
            update_activity_prompt(chosen_id)
        elif view_update_delete.lower() == "d":
            delete_activity_prompt(chosen_id)
        elif view_update_delete.lower() == "a":
            attach_photo_or_category_to_activity(chosen_id)
        else:
            multi_choice_error()
    elif correct_yn == "n":
        view_activities()
    else:
        y_n_error()


def view_activity(chosen_id):
    start = chosen_id
    end = chosen_id + 1
    global last_page
    last_page = view_activities
    display_table(start, end, real_id=True)
    back_exit_or_mm = input(
        "Enter 'back' to return to the activities list, 'exit' to quit, or 'mm' for the main menu: "
    ).strip()
    if back_exit_or_mm == "back":
        view_activities()
    elif back_exit_or_mm == "mm":
        main_menu()
    elif back_exit_or_mm == "exit":
        exit()
    else:
        multi_choice_error()


def update_activity_prompt(chosen_id):
    global last_page
    last_page = view_activities
    activity = session.query(Activity).all()[chosen_id]

    clear_terminal()
    print(f"Currently Selected Activity:\n\n{activity}\n")
    new_name = input(
        "Type a new name for this activity or press Enter to keep the current name: "
    ).strip()

    if new_name:
        activity.name = new_name

    new_description = input("Enter new description or press Enter to skip: ").strip()
    if new_description:
        activity.description = new_description

    new_note = input("Enter new note or press Enter to skip: ").strip()
    if new_note:
        activity.notes = new_note

    new_location = input("Enter new location or press Enter to skip: ").strip()
    if new_location:
        activity.location = new_location

    new_weather = input(
        "Enter new weather condition ['Clear', 'Cloudy', 'Rainy', 'Snowy', 'Windy', 'Foggy', 'Hot', 'Cold', 'Mild', or 'Sunny'] or press Enter to skip: "
    ).strip()
    if new_weather:
        activity.weather = new_weather

    new_date = input("Enter new date or press Enter to skip: ").strip()
    if new_date:
        activity.date = new_date
    clear_terminal()
    print(activity)
    print("\n\nWould you like to update this activity?")
    update_yn = input("y/n: ").strip()
    if update_yn == "y":
        session.commit()
        clear_terminal()
        print("Activity updated successfully!")
        time.sleep(2)
        main_menu()
    if update_yn == "n":
        view_activities()
    else:
        y_n_error()


def delete_activity_prompt(chosen_id):
    global last_page
    last_page = view_activities
    activity_to_delete = Activity.get_all_activities(session)[chosen_id]
    clear_terminal()
    correct_activity = input(
        f"Are you sure you wish to delete the activity: '{activity_to_delete.name}'? [y/n]: "
    )

    if correct_activity == "y":
        session.delete(activity_to_delete)
        session.commit()
        print(f"You have successfully deleted {activity_to_delete.name}")
        time.sleep(2)
        main_menu()
    elif correct_activity == "n":
        view_activities()
    else:
        y_n_error


def create_activity():
    clear_terminal()
    print("New Activity Creation".center(width))
    activity_instance = dict()
    activity_name = input("Enter the name of the activity: ").strip()
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
                                new_activity = Activity(
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


def view_activities_based_on_category():
    global last_page
    last_page = activities_menu
    clear_terminal()
    categories = session.query(Category).all()
    print(
        f"Available Categories: {[f'{index + 1}: {category.category_name}' for index, category in enumerate(categories)]}\n"
    )
    category = input(
        'Select a category by its corresponding number or enter "back" to return to the Activities Menu: '
    )
    if category == "back":
        activities_menu()
    elif int(category) in range(1, len(categories) + 1):
        category = int(category)
        category_chosen = categories[category - 1]
        clear_terminal()
        print(f"You have chosen [{category_chosen.category_name}]")
        time.sleep(1.5)
        display_table(
            start=0,
            end=len(category_chosen.activities),
            category_filter=True,
            category_chosen=category_chosen,
        )
        i_hate_naming_things = input(
            "\n\nPress any key and then 'Enter' to go back to the main menu: "
        )
        if i_hate_naming_things:
            main_menu()
        else:
            main_menu()
    else:
        multi_choice_error()


def attach_photo_or_category_to_activity(chosen_index):
    global last_page
    last_page = view_activities
    activity = session.query(Activity).all()[chosen_index]
    categories = session.query(Category).all()
    clear_terminal()
    photo_or_category = input(
        f"Would you like to attach a photo or a category to [{activity.name}]?\n\nType 'p' for photo, 'c' for category, or 'back' to go back to Activities Table: \n\n"
    )
    if photo_or_category == "back":
        view_activities()
    elif photo_or_category == "p":
        clear_terminal()
        photo_description = input("Please enter the new photo description: ")
        if photo_description:
            photo_url = input("\n\nPlease enter the new photo url : ")
            if is_valid_image(photo_url):
                new_photo = Photo(photo_description=photo_description, url=photo_url)
                activity.photos.append(new_photo)
                session.add(new_photo)
                session.commit()
                clear_terminal()
                print("New photo has been added to the database.").center(width)
                time.sleep(2)
                main_menu()
            else:
                clear_terminal()
                print(
                    'The photo must end in ["jpeg", "png", "pdf", "jpg", "heic"]. Please try again.'
                )
                time.sleep(2)
                attach_photo_or_category_to_activity(chosen_index)
        else:
            view_activities()
    elif photo_or_category == "c":
        clear_terminal()
        print(
            f'Here are your current categories. {[f"{index + 1}: {category.category_name}" for index,category in enumerate(categories)]}\n'
        )
        category_option = input(
            "Please select an option that corresponds to a category to attach to an activity."
        )
        if int(category_option) in range(1, len(categories) + 1):
            clear_terminal()
            category_option = int(category_option)
            category_chosen = session.query(Category).all()[category_option - 1]
            correct_option = input(
                f"Would you like to attach [{category_chosen.category_name}] to [{activity.name}]? \n\ny/n :"
            )
            if correct_option == "y":
                activity.categories.append(category_chosen)
                session.commit()
                clear_terminal()
                print(
                    f"You have added [{category_chosen.category_name}] to [{activity.name}]!"
                )
                time.sleep(2)
                main_menu()
            elif correct_option == "n":
                view_activities()
            else:
                y_n_error()
        else:
            multi_choice_error()
    else:
        multi_choice_error()


def categories_menu():
    global last_page
    last_page = categories_menu
    clear_terminal()
    print("Category Management\n".center(width))
    print(
        "Select an option:\n\n1: Create a New Category\n\n2: Modify an Existing Category\n\n3: Remove a Category\n"
    )
    category_option = input("Enter 1, 2, or 3, or type 'exit' or 'back': ").strip()

    if category_option.lower() == "exit":
        exit()
    elif category_option.lower() == "back":
        main_menu()
    elif category_option in ["1", "2", "3"]:
        if category_option == "1":
            create_category_prompt()
        elif category_option == "2":
            update_category_prompt()
        elif category_option == "3":
            delete_category_prompt()
    else:
        multi_choice_error()
        categories_menu()


def create_category_prompt():
    clear_terminal()
    global last_page
    last_page = categories_menu
    categories = session.query(Category).all()
    print(
        "Existing Categories: "
        + f"{[category.category_name for category in categories]}\n"
    )
    category_name = input(
        "Enter the name for the new category or type 'back': "
    ).strip()
    if not 0 < len(category_name) <= 32:
        print("The category name but be in between 0 and 33 characters.")
        create_category_prompt()
    elif category_name == "back":
        categories_menu()
    else:
        new_category = Category(category_name=category_name)
        if new_category:
            clear_terminal()
            print(
                f"Are you sure you want to create the category: {new_category.category_name}?"
            )
            y_n_answer = input("y/n : ").strip()
            if y_n_answer == "y":
                session.add(new_category)
                session.commit()
                clear_terminal()
                print(f"You have added {new_category.category_name}!")
                time.sleep(2)
                main_menu()
            elif y_n_answer == "n":
                categories_menu()
            else:
                y_n_error()
        else:
            main_menu()


def update_category_prompt():
    global last_page
    last_page = categories_menu
    categories = session.query(Category).all()
    clear_terminal()
    print("Current Categories:")
    print("-" * 19)
    for index, category in enumerate(categories):
        print(f"{index + 1}. {category.category_name}")
    print("\n")

    category_to_update = input(
        "Select a category number to update or type 'back' to go back: "
    ).strip()
    if category_to_update == "back":
        categories_menu()
    elif int(category_to_update) in range(1, (len(categories) + 1)):
        category_to_update = int(category_to_update)
        category_chosen = categories[category_to_update - 1]
        clear_terminal()
        y_n_correct = input(
            f"Is this the category you wanted to select [{category_chosen.category_name}]? y/n  :  "
        ).strip()
        if y_n_correct == "y":
            print(f"What would you like to change {category_chosen.category_name} to? ")
            new_category_name = input("")
            clear_terminal()
            if 0 < len(new_category_name) < 16:
                im_running_out_of_names_for_these_inputs = input(
                    f"Is '{new_category_name}' correct?: y/n   "
                ).strip()
                if im_running_out_of_names_for_these_inputs == "y":
                    category_chosen.category_name = new_category_name
                    session.commit()
                    clear_terminal()
                    print("the Category has been updated!")
                    time.sleep(2)
                    main_menu()
                elif im_running_out_of_names_for_these_inputs == "n":
                    categories_menu()
                else:
                    y_n_error()
            else:
                print("The new category name must be in between 0 and 17 characters.")
                time.sleep(2)
                categories_menu()
        elif y_n_correct == "n":
            categories_menu()
        else:
            y_n_error()
    else:
        multi_choice_error()


def delete_category_prompt():
    global last_page
    last_page = categories_menu
    categories_to_delete = session.query(Category).all()
    clear_terminal()
    print("Current Categories for Deletion:")
    print("-" * 32)
    for index, category in enumerate(categories_to_delete):
        print(f"{index + 1}. {category.category_name}")
    print("\n")

    to_delete = input("Select a category number to delete or type 'back' to go back: ")

    if to_delete.isdigit():
        to_delete = int(to_delete)
        clear_terminal()
        category_to_delete = categories_to_delete[to_delete - 1]
        yn_to_delete = input(
            f"Is this the category you would like to delete? [{category_to_delete.category_name}]\n\ny/n: "
        )
        if yn_to_delete == "y":
            session.delete(category_to_delete)
            session.commit()
            clear_terminal()
            print(f"You have successfully deleted {category_to_delete.category_name}")
            time.sleep(2)
            main_menu()
        elif yn_to_delete == "n":
            categories_menu()
        else:
            y_n_error()
    elif to_delete == "back":
        categories_menu()
    else:
        multi_choice_error()


def photo_menu():
    global last_page
    last_page = main_menu
    clear_terminal()
    print("Photo Menu\n\n".center(width))
    print(
        "1: View Photo Table\n\n2: If you're looking to create a new photo, follow the instructions in Activities Table. Entering '2' will take you there."
    )
    print("\n")

    photo_menu_choice = input("Select an option [1,2, exit, back]: ")
    if photo_menu_choice.lower() == "back":
        main_menu()
    elif photo_menu_choice.lower() == "exit":
        exit()
    elif photo_menu_choice in ["1", "2"]:
        if photo_menu_choice == "1":
            view_photo_table()
        elif photo_menu_choice == "2":
            view_activities()
        else:
            multi_choice_error()
    else:
        multi_choice_error()


def view_photo_table():
    global last_page
    last_page = view_photo_table
    start = 0
    end = 10
    total_photos = len(session.query(Photo).all())

    display_table(start, end, entity_type="photo")

    loop = True
    while loop:
        if end >= total_photos:
            user_input_table = input(
                "Type 'p' for previous, an ID to view or update a photo, 'back', or 'exit': "
            ).strip()
        elif start == 0:
            user_input_table = input(
                "Type 'n' for next to see the next 10 photos, an ID to view or update a photo, 'back', or 'exit': "
            ).strip()
        else:
            user_input_table = input(
                "Type 'n' for next to see the next 10 photos, 'p' for previous to see previous 10, an ID to view or update a photo, 'back', or 'exit': "
            ).strip()

        if user_input_table.isdigit():
            chosen_index = int(user_input_table) - 1
            photo = session.query(Photo).all()[chosen_index]
            if photo:
                loop = False
                clear_terminal()
                print(f"You have chosen [{photo.photo_description}]. Is that correct?")
                photo_chosen = input("y/n : ")
                if photo_chosen == "y":
                    clear_terminal()
                    print(
                        "Type 'd' to delete this photo, or 'u' to update this photos information.\n\n"
                    )
                    to_update_delete = input("d/u: ")
                    if to_update_delete == "d":
                        clear_terminal()
                        to_delete = input(
                            f"Are you sure you want to delete [{photo.photo_description}]?\n\ny/n: "
                        )
                        if to_delete == "y":
                            clear_terminal()
                            session.delete(photo)
                            session.commit()
                            print(f"[{photo.photo_description}] was deleted!")
                            time.sleep(2)
                            main_menu()
                        elif to_delete == "n":
                            view_photo_table()
                        else:
                            y_n_error()
                    elif to_update_delete == "u":
                        update_photo_prompt(photo)
                    else:
                        multi_choice_error()
                elif photo_chosen == "n":
                    view_photo_table()
                else:
                    y_n_error()
            else:
                clear_terminal()
                print("No photo found with the specified ID.")
                time.sleep(2)
                view_photo_table()
        elif user_input_table.lower() == "n" and end < total_photos:
            start += 10
            end += 10
            if end > total_photos:
                end = total_photos
            display_table(start, end, entity_type="photo")
        elif user_input_table.lower() == "p" and start > 0:
            start -= 10
            end = start + 10
            display_table(start, end, entity_type="photo")
        elif user_input_table.lower() == "back":
            loop = False
            photo_menu()
        elif user_input_table.lower() == "exit":
            loop = False
            exit()
        else:
            multi_choice_error()
            display_table(start, end, entity_type="photo")


def update_photo_prompt(photo_chosen):
    global last_page
    last_page = view_photo_table
    clear_terminal()
    print("Update Photo Information".center(width))

    new_photo_description = input("New description (Press enter to skip): ")
    if new_photo_description:
        photo_chosen.photo_description = new_photo_description
    new_photo_url = input("Enter new photo URL (Press enter to skip): ")
    if new_photo_url and is_valid_image(new_photo_url):
        photo_chosen.url = new_photo_url
    clear_terminal()
    if new_photo_description or new_photo_url:
        print(
            f"Are you sure this look correct?\n\nPhoto Description: {new_photo_description if new_photo_description else photo_chosen.photo_description}\n\nPhoto URL: [{new_photo_url if new_photo_url else photo_chosen.url}]?\n\n"
        )
        update_photo = input("y/n: ")
        if update_photo == "y":
            session.commit()
            clear_terminal()
            print(f"{photo_chosen.photo_description} has been updated!")
            time.sleep(2)
            main_menu()
        elif update_photo == "n":
            view_photo_table()
        else:
            y_n_error()
    else:
        view_photo_table()


def display_table(
    start,
    end,
    category_filter=None,
    category_chosen=None,
    real_id=False,
    entity_type="activity",
):
    if entity_type == "activity":
        if category_filter:
            items = category_chosen.activities
        else:
            items = Activity.get_all_activities(session)
        if real_id:
            item_ids = [item.id for item in items[start:end]]
            field_names = [
                "Table ID",
                "Activity",
                "Location",
                "Weather",
                "Notes",
                "Date",
            ]
        else:
            item_ids = list(range(start + 1, end + 1))
            field_names = ["ID", "Activity", "Location", "Weather", "Notes", "Date"]
        get_data = lambda item: [
            item.name,
            item.location,
            item.weather,
            item.notes,
            f"{item.date.month}-{item.date.day}-{item.date.year}",
        ]
        header = "Activities Table"
    elif entity_type == "photo":
        items = session.query(Photo).all()
        item_ids = list(range(start + 1, end + 1))
        field_names = [
            "Photo ID",
            "Photo Description",
            "Photo URL",
            "Connected Activity",
        ]
        get_data = lambda item: [item.photo_description, item.url, item.activity.name]
        header = "Photos Table"

    sliced_items = items[start:end]
    table = PrettyTable()
    table.field_names = field_names

    for item_id, item in zip(item_ids, sliced_items):
        row_data = [item_id] + get_data(item)
        table.add_row(row_data)

    clear_terminal()
    table_str = table.get_string()
    centered_table = "\n".join([line.center(width) for line in table_str.split("\n")])

    print(header.center(width))
    print(centered_table)

    if category_filter and entity_type == "activity":
        category_filter_str = table.get_string()
        centered_category_filtered_table = "\n".join(
            [line.center(width) for line in category_filter_str.split("\n")]
        )
        clear_terminal()
        print(f"Activities in {category_chosen.category_name}".center(width))
        print(centered_category_filtered_table)

        table_str = table.get_string()
        centered_table = "\n".join(
            [line.center(width) for line in table_str.split("\n")]
        )

        clear_terminal()
        print("Activities Table".center(width))
        print(centered_table)


def exit():
    clear_terminal()
    print("Are you sure you want to exit?\n")
    exit_y_or_n = input("y/n: ").strip()
    if exit_y_or_n.lower() == "y":
        print("Goodbye!")
        time.sleep(1)
        clear_terminal()
    elif exit_y_or_n.lower() == "n":
        clear_terminal()
        if last_page:
            last_page()
        else:
            main_menu()
    else:
        y_n_error()
        clear_terminal()


def clear_terminal():
    print("\n" * 32)


def multi_choice_error():
    global last_page
    clear_terminal()
    print("Input must correspond to an option.")
    time.sleep(2)
    if last_page:
        last_page()
    else:
        main_menu()


def y_n_error():
    global last_page
    clear_terminal()
    print("Input must be 'y' for yes or 'n' for no.")
    time.sleep(2)
    if last_page:
        last_page()
    else:
        main_menu()


def is_valid_date(date_str):
    try:
        date.fromisoformat(date_str)
        return True
    except ValueError:
        return False


def is_valid_image(source):
    allowed_extensions = ["jpeg", "png", "pdf", "jpg", "heic"]
    extension = source.split(".")[-1]
    return extension.lower() in allowed_extensions


if __name__ == "__main__":
    start()
