# CS425 Linkedin Project

**LINK to video** https://www.loom.com/share/05e8d25393fd4092bca7abb5b1f7c9e7?sid=490d0cd4-1587-4beb-aa0b-f23024729ca3 

A brief description of your project, what it does, and its purpose.

## Table of Contents

1. [Installation](#installation)
2. [Steps to Run](#steps-to-run)
3. [File Description](#file-description)

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:rayan1242/Linkedin-Fullstack-Application.git
   cd Linkedin-Fullstack-Application
   ```
2. **Install dependencies:**
   ```bash
   pip install mysql-connector-python
   pip install tabulate
   cd front-end
   npm i
   ```

## Steps to Run

1. **Create the Database:**
   Use the provided SQL dump file to create the database. You can import the dump into your MySQL server using a command like:

   ```bash
   mysql -u your_username -p < DumpLinkedin.sql
   ```

   **OR**

   Open DumpLinkedin.sql in your MySqlWorkbench and run it

2. **Update Database Credentials:**
   Open the src/db.py file and modify the database connection credentials to match your setup:

   ```bash
    user = 'your_username'
    password = 'your_password'
    host = 'localhost' # or your database host
    database = 'your_database_name'
   ```

3. **Run application:**

   ```bash
   python3 src/index.py
   ```

   
   ```bash
   cd front-end
   npm run dev
   ```

4. **Go to the link in the terminal to use the application**

## File Description

- main.py: entry, main menu.
- application.py: CRUD of application table.
- education.py: CRUD of education table.
- experience.py: CRUD of experience table.
- institution.py: CRUD of institution table.
- job.py: CRUD of job table.
- post.py: CRUD of post table.
- skill.py: CRUD of skill table.
- user.py: CRUD of user table.
- front-end/src/lib: API, types
- front-end/src/routes: all routes
