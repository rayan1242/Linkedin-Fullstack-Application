# CS425 Linkedin Project

A brief description of your project, what it does, and its purpose.

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Steps to Run](#steps-to-run)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Adi-shinde31/CS425-Linkedin-Project
   cd CS425-Linkedin-Project
   ```
2. **Install dependencies:**
   ```bash
   pip install mysql-connector-python
   pip install tabulate
   ```

## Usage

## Steps to Run

1. **Create the Database:**
   Use the provided SQL dump file to create the database. You can import the dump into your MySQL server using a command like:
   ```bash
    mysql -u your_username -p < dump.sql
   ```
2. **Create the Database:**
   Open the src/db.py file and modify the database connection credentials to match your setup:

   ```bash
    user = 'your_username'
    password = 'your_password'
    host = 'localhost'
    database = 'your_database_name'
   ```

3. **Access Different Tables/Description of files:**
   Run main.py or the following files to access the corresponding tables in the database:

   - main.py: entry, main menu.
   - application.py: CRUD of application table.
   - education.py: get_all_education, CRUD of education table.
   - experience.py: CRUD of experience table.
   - institution.py: get_all_institutions, CRUD of institution table.
   - job.py: get_all_jobs, CRUD of job table.
   - post.py: get_all_posts, CRUD of post table.
   - skill.py: get_all_skills, CRUD of skill table.
   - user.py: get_all_users, CRUD of user table.
