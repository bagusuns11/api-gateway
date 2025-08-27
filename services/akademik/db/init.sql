CREATE DATABASE IF NOT EXISTS akademik_db;
USE akademik_db;

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    major VARCHAR(100)
);

-- Menambahkan 10 record sampel
INSERT INTO students (name, major) VALUES 
('John Doe', 'Computer Science'),
('Jane Smith', 'Mathematics'),
('Alice Johnson', 'Engineering'),
('Bob Brown', 'Physics'),
('Charlie Davis', 'Biology'),
('David Wilson', 'Economics'),
('Eva Martinez', 'Literature'),
('Frank Garcia', 'Chemistry'),
('Grace Lee', 'Business'),
('Henry Kim', 'Psychology');
