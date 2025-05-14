-- Database: Library Management System

-- Table: Members
CREATE TABLE members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Table: Authors
CREATE TABLE authors (
    author_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Table: Genres
CREATE TABLE genres (
    genre_id INT AUTO_INCREMENT PRIMARY KEY,
    genre_name VARCHAR(50) UNIQUE NOT NULL
);

-- Table: Books
CREATE TABLE books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    publication_year INT,
    publisher VARCHAR(100),
    total_copies INT NOT NULL DEFAULT 1,
    available_copies INT NOT NULL DEFAULT 1,
    genre_id INT,
    FOREIGN KEY (genre_id) REFERENCES genres(genre_id)
);

-- Table: Book_Authors (Many-to-Many relationship between Books and Authors)
CREATE TABLE book_authors (
    book_id INT,
    author_id INT,
    PRIMARY KEY (book_id, author_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(author_id) ON DELETE CASCADE
);

-- Table: Loans
CREATE TABLE loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    return_date DATE,
    due_date DATE NOT NULL,
    FOREIGN KEY (book_id) REFERENCES books(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES members(member_id) ON DELETE CASCADE
);

-- Sample Data
INSERT INTO members (first_name, last_name, email, phone_number, address) VALUES
('Alice', 'Smith', 'alice.smith@example.com', '123-456-7890', '123 Main St'),
('Bob', 'Johnson', 'bob.johnson@example.com', '987-654-3210', '456 Oak Ave');

INSERT INTO authors (first_name, last_name) VALUES
('Jane', 'Doe'),
('John', 'Smith');

INSERT INTO genres (genre_name) VALUES
('Fiction'),
('Science Fiction'),
('Mystery');

INSERT INTO books (title, isbn, publication_year, publisher, total_copies, available_copies, genre_id) VALUES
('The Great Novel', '978-1234567890', 2020, 'Acme Books', 5, 5, 1),
('Space Odyssey 2001', '978-0987654321', 1968, 'Galaxy Publishing', 3, 3, 2),
('The Secret Case', '978-1122334455', 2022, 'Mystery House', 4, 4, 3);

INSERT INTO book_authors (book_id, author_id) VALUES
(1, 1),
(2, 2),
(3, 1);

INSERT INTO loans (book_id, member_id, due_date) VALUES
(1, 1, '2025-05-28'),
(2, 2, '2025-05-21');