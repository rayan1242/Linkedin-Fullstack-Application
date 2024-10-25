import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_job(connection):
    cursor = connection.cursor()

    institution_id = input("\nEnter institution ID: ")
    job_title = input("Enter job title: ")
    description = input("Enter description: ")
    job_type = input("Enter type: ")

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
    try:
        institution_id = int(institution_id)
    except ValueError:
        print("Error: Institution ID must be an integer.")
        return

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

    job_id = input("\nEnter job ID: ")
    
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return    
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    try:
        query = "SELECT * FROM job WHERE job_id = %s"
        cursor.execute(query, (job_id,))
        result = cursor.fetchone()
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

    job_id = input("\nEnter job ID to update: ")
    
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    
    fields = ["institution_id", "job_title", "description", "type"]
    updates = []
    values = []
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

    if not updates:
        print("No fields to update")
        return
    try:
        query = f"UPDATE job SET {', '.join(updates)} WHERE job_id = %s"
        values.append(job_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        print("\nJob updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    

def delete_job(connection):
    cursor = connection.cursor()

    job_id = input("Enter job ID to delete: ")
    
    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    try:
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
