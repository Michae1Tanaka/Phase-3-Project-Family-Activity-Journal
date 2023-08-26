# Flatiron School Phase 3 Project: Family Activity Journal

# Introduction

Welcome to my phase 3 project, a terminal-based Python application. Leveraging the power of Python, SQLAlchemy, SQLite, and Alembic, users can navigate various 'pages' inside the terminal to view activities based on categories, view tables of activities or photos, create new activities, and even attach photos to a specific activity that will be reflected inside the database.

# Installation

1. Fork the repository [here](https://github.com/Michae1Tanaka/Phase-3-Project-Family-Activity-Journal)
2. Copy the SSH key
3. Navigate to the folder in which you would like to repository to be placed.
4. Type `git clone` and then paste the SSH key. It should look something like this `git clone https://github.com/Michae1Tanaka/Phase-3-Project-Family-Activity-Journal`
5. Navigate to the project directory
6. Open the IDE of your choosing.
7. Open the terminal and type `pipenv install` to get started.
8. If you'd like to test the functionality of the application, in the terminal type `python -m lib.db.seed`. This will fill the database with fake seed data.
9. In order to open the application in the terminal type in `python -m lib.cli`. Make sure you're inside the Family-Activity-Journal directory.
10. If you're done using seed data, exit the application and type in the terminal `python -m lib.helpers.setup_database` to wipe the database of fake seed data and begin creating your own memories!

# Contributor's Guide

I encourage any contributions to my family activity journal application. Anything and everything is appreciated. Here are some guidelines to follow if you'd like to contribute:

1. **Fork and Clone the Repository**:
   Begin by following the instructions in the [Installation](#installation) portion of the README.md. Be sure to check that your fork is the "origin" remote with `git remote -v`. If you do not see an "origin" remote, you can add it using `git remote add origin https://github.com<your-username>/phase-2-project-fitness-tracker-app-frontend.git`. Replace `<your-username>` with your GitHub username.
2. **Set up Development Environment**:
   After forking and cloning the repository, contributors should create a new branch on which they can make their changes. This can be done using the command git checkout -b <branch-name>. Replace <branch-name> with a name that describes the feature or bugfix the contributor will be working on. In addition, contributors may need to install any necessary dependencies for the project using `pipenv install`.
3. **Work on Your Own Feature or a Bug fix**:
   Contributors should pick a feature to add or a bug to fix. Ideally, this should be something that they've discussed with myself to ensure it's something the project needs. Contributors may want to create a detailed plan or outline for how they're going to implement the feature or fix the bug to keep themselves organized and ensure they've thought through the problem.
4. **Make Changes in Your Local Repo**:
   After picking a feature or bugfix and planning their approach, contributors should make the changes in their local copy of the repository. This might involve adding new files or modifying existing ones.
5. **Commit your changes**:
   As contributors make changes, they should regularly commit these changes to their branch. Each commit should be a logical chunk of work and should include a clear, concise message that describes the change. This can be done using the command git commit -m "Your descriptive message here".
6. **Push Your Changes to Your Fork**:
   Once they've made their changes and committed them to their branch, contributors should push their branch to their fork of the repository on GitHub. This can be done using the command git push origin <branch-name>.
7. **Begin the Pull Request**:
   After pushing their changes to GitHub, contributors can start a pull request on the original repository. To do this, they should navigate to their fork of the repository on GitHub, switch to their branch, and click the "New pull request" button.
8. **Create the Pull Request**:
   When creating the pull request, contributors should provide a title and description that explains what the changes do and why they should be included in the project. Once they've filled out this information, they can click "Create pull request". Then, it's up to me to review the changes and decide whether to merge them into the project.

## Credits

This projects tables are produced with [PrettyTable by Luke Maurits](https://pypi.org/project/prettytable/). Fake seed data is created using [Faker by Daniele Faraglia](https://faker.readthedocs.io/en/master/). Data migrations are handled using [Alembic by Mike Bayer](https://alembic.sqlalchemy.org/en/latest/index.html). Database is created by [SQLite](https://www.sqlite.org/index.html) and the [team behind it.](https://www.sqlite.org/crew.html) Database interaction and ORM (Object-Relational-Mapping) are facilitated with [SQLAlchemy also by Mike Bayer](https://docs.sqlalchemy.org/en/20/).

## License

MIT License

Copyright (c) [2023] [Michael Tanaka]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
