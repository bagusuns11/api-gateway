CREATE DATABASE IF NOT EXISTS kepegawaian_db;
USE kepegawaian_db;

CREATE TABLE IF NOT EXISTS employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);

-- Menambahkan 10 record sampel
INSERT INTO employees (name, position) VALUES
('Alice', 'Lecturer'),
('Bob', 'Administrator'),
('Charlie', 'Janitor'),
('David', 'Technician'),
('Eva', 'Professor'),
('Frank', 'Secretary'),
('Grace', 'Researcher'),
('Henry', 'Assistant Professor'),
('Isabella', 'Laboratory Technician'),
('James', 'HR Specialist');
