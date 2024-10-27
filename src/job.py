import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_job(connection):
    cursor = connection.cursor()

    # Prompt the user for job details
    institution_id = input("\nEnter institution ID: ")
    job_title = input("Enter job title: ")
    description = input("Enter description: ")
    job_type = input("Enter type: ")

    # Validate that none of the inputs are empty
    if(institution_id==""):
        print("Error: Institution ID cannot be empty.")
        return
    if(job_title==""):
        print("Error: Job title cannot be empty.")
        return
    if(description==""):
        print("Error: Description cannot be empty.")
        return
    if(job_type==""):
        print("Error: Type cannot be empty.")
        return
    
    # Convert institution_id to an integer and check for valid type inputs
    try:
        institution_id = int(institution_id)
    except ValueError:
        print("Error: Institution ID must be an integer.")
        return

    # Additional validation checks for data types of the inputs
    if not isinstance(job_title, str):
        print("Error: Job title must be a string.")
        return

    if not isinstance(description, str):
        print("Error: Description must be a string.")
        return

    if not isinstance(job_type, str):
        print("Error: Type must be a string.")
        return
    
    try:
        # Prepare and execute the SQL insert query
        query = """INSERT INTO job (institution_id, job_title, description, type)
                     VALUES (%s, %s, %s, %s)"""
        values = (institution_id, job_title, description, job_type)
        cursor.execute(query, values)   
        connection.commit()
        job_id = cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return job_id



def read_job(connection):
    cursor = connection.cursor(dictionary=True)

    # Prompt the user to enter the job ID
    job_id = input("\nEnter job ID: ")
    
    # Validate that job ID is not empty
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return    
    
    # Validate that job ID is a numeric string
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    
    try:
        # Prepare and execute the SQL query to select the job record with the specified ID
        query = "SELECT * FROM job WHERE job_id = %s"
        cursor.execute(query, (job_id,))
        result = cursor.fetchone()

        # If a job is found, print the job details in a formatted table
        if result:
                print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Job not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def get_all_jobs(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM job"
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        result = None

    if result:
        # Prepare the data for tabulate
        table_data = []
        for record in result:
            table_data.append([
                record['institution_id'],
                record['job_title'],
                record['description'],
                record['type']
            ])

        # Print the table
        print(tabulate(table_data, headers=["institution_id", "job_title", "description", "job_type"], tablefmt="grid"))
    else:
        print("No job records found.")

    cursor.close()

def update_job(connection):
    cursor = connection.cursor()

    # Prompt the user to enter the Job ID for the job to be updated
    job_id = input("\nEnter job ID to update: ")
    
    # Validate that Job ID is not empty and is a number
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    
    # Define the fields that can be updated
    fields = ["institution_id", "job_title", "description", "type"]
    updates = []
    values = []

    # Loop through each field and prompt the user for a new value if they wish to update it
    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            if field == "institution_id":
                try:
                    value = int(value)
                except ValueError:
                    print("Error: Institution ID must be an integer.")
                    return
            updates.append(f"{field} = %s")
            values.append(value)

    # If no fields were updated, exit the function
    if not updates:
        print("No fields to update")
        return
        
    try:
        # Prepare the SQL update query
        query = f"UPDATE job SET {', '.join(updates)} WHERE job_id = %s"
        values.append(job_id)

        # Execute the query with the updated values
        cursor.execute(query, tuple(values))
        connection.commit()

        print("\nJob updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    

def delete_job(connection):
    cursor = connection.cursor()

    # Prompt the user to enter the Job ID for the job to be deleted
    job_id = input("Enter job ID to delete: ")
    
    # Validate that Job ID is not empty and is a number
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    
    try:
        # Prepare the SQL delete query to remove the job with the specified ID
        query = "DELETE FROM job WHERE job_id = %s"
        cursor.execute(query, (job_id,))
        connection.commit()
        print("Job deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")  
    finally:
        cursor.close()

def job_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create job")
        print("2: Read job")
        print("3: Get all job records")
        print("4: Update job")
        print("5: Delete job")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_job(connection)
        elif choice == '2':
            read_job(connection)
        elif choice == '3':
            get_all_jobs(connection)
        elif choice == '4':
            update_job(connection)
        elif choice == '5':
            delete_job(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Job Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
