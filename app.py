import subprocess

# Database connection details

# PostgreSQL Database name
DB_NAME = "school_db"

# PostgreSQL username
# CHANGE USERNAME IF NOT POSTGRES!!!!
DB_USER = "postgres" 

def run_sql(command):
    # Execute an SQL command using psql
    try:
        full_cmd = f'psql -U {DB_USER} -d {DB_NAME} -c "{command}"'
        subprocess.run(full_cmd, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")

# Easier to manage tests and stuff, default data
def resetTable():
    # Resets the table to the default data
    print("\n--- Resetting students table ---")

    # Deletes current data
    run_sql("DELETE FROM students;")

    # Resets ID
    run_sql("ALTER SEQUENCE students_student_id_seq RESTART WITH 1;")
    
    # Inserts init data
    run_sql("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES "
            "('John', 'Doe', 'john.doe@example.com', '2023-09-01'), "
            "('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), "
            "('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02');")
    
    # # shows data
    # getAllStudents()

def getAllStudents():
    # Retrieve and display all students in order of id
    print("\n--- All Students ---")
    run_sql("SELECT * FROM students ORDER BY student_id;")

def addStudent(first_name, last_name, email, enrollment_date):
    # Insert a new student record in stu table
    command = f"INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES ('{first_name}', '{last_name}', '{email}', '{enrollment_date}');"
    run_sql(command)
    print(f"Added {first_name} {last_name}.")
    # Decided not to display table after every command, but can
    # getAllStudents()

def updateStudentEmail(student_id, new_email):
    # Update a student's email via student id
    command = f"UPDATE students SET email = '{new_email}' WHERE student_id = {student_id};"
    run_sql(command)
    print(f"Updated email for student_id {student_id}.")
    # getAllStudents()

def deleteStudent(student_id):
    # Delete a student by ID
    command = f"DELETE FROM students WHERE student_id = {student_id};"
    run_sql(command)
    print(f"Deleted student with ID {student_id}.")
    # getAllStudents()

def main():
    while True:
        # Menu to choose operation
        print("\nChoose an operation:")
        print("1. Show all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Reset table to initial data")
        print("0. Exit")
        
        # takes user input
        choice = input("Enter your choice: ").strip()
        
        # Menu logic
        if choice == "1":
            getAllStudents()
        elif choice == "2":
            # Allows user to write first/last name, email and enrollment date
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            date = input("Enrollment Date (YYYY-MM-DD): ")
            addStudent(first, last, email, date)
        elif choice == "3":
            # Select the student to update
            sid = input("Student ID to update: ")
            email = input("New Email: ")
            updateStudentEmail(sid, email)
        elif choice == "4":
            # Takes student by id to delete
            sid = input("Student ID to delete: ")
            deleteStudent(sid)
        elif choice == "5":
            # Resets
            resetTable()
        elif choice == "0":
            # To exit
            print("Exiting...")
            break
        else:
            # Invalid option
            print("Invalid choice! Please try again.")

# Main
if __name__ == "__main__":
    main()
