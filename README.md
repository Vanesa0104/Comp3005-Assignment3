# Comp 3005 - Assignment 3

## Description

This is a Python application to manage a students database using PostgreSQL.
The application allows you to:

* View all students
* Add a new student
* Update a student's email
* Delete a student
  And a little personal touch I added, is the option to...
* Reset the table to initial data

The database operations are executed through Python using the `subprocess` module and `psql`.

---

## Setup

1. Open **psql** and connect to your PostgreSQL server:

```
C:\Users\SomeUser\Downloads\Comp 3005\Assignment 3>psql -U postgres
Password for user postgres: ENTER YOUR PASSWORD
```

2. Create the database:

```sql
CREATE DATABASE school_db;
```

3. Connect to the database:

```sql
\c school_db;
```

4. Execute the SQL script to create the `students` table and insert initial data:


```sql
\i 'C:/Users/SomeUser/Path to file xxx/db/create_table.sql'
```

**Expected output:**

```
'C:/Users/SomeUser/Path to file xxx/db/create_table.sql:
CREATE TABLE
INSERT 0 3
```

5. Verify the data:

```sql
SELECT * FROM students;
```

**Result:**

```
 student_id | first_name | last_name |         email          | enrollment_date
------------+------------+-----------+------------------------+-----------------
          1 | John       | Doe       | john.doe@example.com   | 2023-09-01
          2 | Jane       | Smith     | jane.smith@example.com | 2023-09-01
          3 | Jim        | Beam      | jim.beam@example.com   | 2023-09-02
(3 rows)
```

---

## How to Run the Application

1. Ensure that Python 3 and PostgreSQL are installed
2. Make sure the `DB_NAME` and `DB_USER` in `app.py` match your PostgreSQL setup.
3. Open a terminal in the project folder and run:

```bash
python app.py
```

4. Follow the menu to perform operations:

```
1. Show all students
2. Add a student
3. Update a student's email
4. Delete a student
5. Reset table to initial data
0. Exit
```

---

## Notes

* The application uses the `subprocess` module to execute SQL commands via `psql`.
* Ensure your PostgreSQL server is running before starting the application.
* No additional Python libraries are required.


## Demonstration Video

A short demonstration video showing:

* Database setup
* Execution of all application functions
* Effects of INSERT, UPDATE, DELETE operations in pgAdmin

**Video Link:** [Add your video link here]

---

