# Library Management System Database

## Description

This project implements a database schema for a Library Management System using MySQL. It includes tables for members, authors, genres, books, and loans, with appropriate relationships and constraints to manage library operations.

## How to Run/Setup

1.  Ensure you have MySQL installed and running on your local machine.
2.  Save the provided `library_management.sql` file.
3.  Open your terminal or command prompt.
4.  Navigate to the directory where you saved the `.sql` file.
5.  Import the SQL file into your MySQL server using the following command:
    ```bash
    mysql -u your_username -p < library_management.sql
    ```
    (Replace `your_username` with your MySQL username and enter your password when prompted.)

## ERD (Entity-Relationship Diagram)


**Relationships:**

* **Members** to **Loans**: One-to-Many (One member can have many loans).
* **Books** to **Loans**: One-to-Many (One book can be involved in many loans).
* **Genres** to **Books**: One-to-Many (One genre can have many books).
* **Books** to **Authors**: Many-to-Many (A book can have multiple authors, and an author can write multiple books), implemented through the `book_authors` junction table.

## Repository Contents

* `library_management.sql`: The SQL file containing the database schema creation statements.
* `README.md`: This file, providing project information and setup instructions.