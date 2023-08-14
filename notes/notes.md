# Phase 3 Project Family Activity Journal

# Minimum Requirements

- [ ] A CLI application that solves a real-world problem and adheres to best practices.
- [ ] A database created and modified with SQLAlchemy ORM with 2 related tables.
- [ ] A well-maintained virtual environment using Pipenv.
- [ ] Proper package structure in your application.
- [ ] Use of lists
- [ ] Use of dicts.

# Stretch Goals

- [ ] A database created and modified with SQLAlchemy ORM with 3+ related tables.
- [ ] Use of many-to-many relationships with SQLAlchemy ORM.
- [ ] Use of Ranges
- [ ] Use of Tuples

# CRUD

## Create

- [ ] As a user, I want to add a new family activity.
      Method: add_activity()
- [ ] As a user, I want to attach photos to an activity to remember our moments.
      Method: add_photos_to_activity()
- [ ] As a user, I want to create a new category to add the tuple filled with category.
      Method: add_category()

## Read

- [ ] As a user, I want to view all the activities my family has done.
      Method: list_all_activities()
- [ ] As a user, I want to categorize the activities (e.g., Outdoor, Indoor, Vacation).
      Method: categorize_activity()
- [ ] As a user, I want to view all activities in a specific category (e.g., all 'Outdoor' activities).
      Method: list_activities_by_category()
- [ ] As a user, I want to see the weather on the day of our activity.
      Method: get_weather_for_activity()
- [ ] As a user, I want to view all the categories available and see how many activities fall under each category.
      Method: list_all_categories_with_counts()

## Update

- [ ] As a user, I want to update a photo
      Method: update_photo()
- [ ] As a user, I want to update a category
      Method: update_category()
- [ ] As a user, I want to update activity details
      Method: update_activity_info() use a dict?

## Delete

- [ ] As a user, I want to remove a photo from an activity.
      Method: remove_photo_from_activity()
- [ ] As a user, I want to delete an activity if I mistakenly added it.
      Method: delete_activity()
- [ ] As a user, I want to delete a category if I have a typo or don't need it.
      Method: delete_category()

# Tables

## Activity

- [ ] ActivityID Integer() primary_key
- [ ] ActivityName String()
- [ ] ActivityDescription String()
- [ ] Notes String() (note for the next time user goes to this activity)
- [ ] Location String()
- [ ] Weather String() OpenWeatherMap api ?

## Photos One-to-Many Activity<>Photos

- [ ] PhotoID Integer() primary_key
- [ ] ActivityID Integer() ForeignKey
- [ ] PhotoURL String()

## Category

- [ ] CategoryID Integer() primary_key
- [ ] Category String()

## ActivityCategory Many-to-Many Activity<>Category

- [ ] ActivityID Integer() ForeignKey
- [ ] CategoryID Integer() ForeignKey

# Imports

SQLAlchemy, DateTime, PrettyTable, Prompt Toolkit?, Colorama, Pyinquirer? (Checkmarks), Click, OpenWeatherMap(via requests)
