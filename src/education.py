import mysql.connector
from tabulate import tabulate

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="linkedin"
        )
        print("Connected to the database successfully")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None

def create_education(connection):
    cursor = connection.cursor()
    user_id = input("Enter User ID: ")
    institution_id = input("Enter Institution ID: ")
    start = input("Enter Start Date (YYYY-MM-DD): ")
    end = input("Enter End Date (YYYY-MM-DD): ")
    course = input("Enter Course: ")

    query = """INSERT INTO education (user_id, institution_id, start, end, course)
               VALUES (%s, %s, %s, %s, %s)"""
    values = (user_id, institution_id, start, end, course)

    cursor.execute(query, values)
    connection.commit()
    education_id = cursor.lastrowid
    print(f"Education record created successfully with ID: {education_id}")
    cursor.close()

def read_education(connection):
    cursor = connection.cursor(dictionary=True)
    user_id = input("Enter User ID to retrieve education records: ")
    query = "SELECT * FROM education WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    results = cursor.fetchall()
    if results:
        print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print("No education records found for this user.")
    cursor.close()

def update_education(connection):
    cursor = connection.cursor()
    education_id = input("Enter Education ID to update: ")
    fields = ["user_id", "institution_id", "start_date", "end_date", "course"]
    updates = []
    values = []

    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("No fields to update")
        return

    query = f"UPDATE education SET {', '.join(updates)} WHERE id = %s"
    values.append(education_id)

    cursor.execute(query, tuple(values))
    connection.commit()
    print("Education record updated successfully")
    cursor.close()

def delete_education(connection):
    cursor = connection.cursor()
    education_id = input("Enter Education ID to delete: ")
    query = "DELETE FROM education WHERE id = %s"
    cursor.execute(query, (education_id,))
    connection.commit()
    print(f"Education record with ID {education_id} deleted successfully")
    cursor.close()

def main():
    connection = connect_to_database()
    if not connection:
        return

    while True:
        print("\nChoose an operation:")
        print("0: Create education record")
        print("1: Read education records")
        print("2: Update education record")
        print("3: Delete education record")
        print("4: Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == '0':
            create_education(connection)
        elif choice == '1':
            read_education(connection)
        elif choice == '2':
            update_education(connection)
        elif choice == '3':
            delete_education(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()