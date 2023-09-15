CREATE DATABASE IF NOT EXISTS mydb;
USE mydb;

DROP TABLE IF EXISTS my_table;
CREATE TABLE my_table(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT
);

INSERT INTO my_table(name, description) VALUES
    ('John', 'John is a common English name and is derived from the Hebrew name Yohanan.'),
    ('Alice', 'Alice is of Old German origin, meaning "noble". It is often associated with fairy tales and adventures.'),
    ('Bob', 'Bob is a diminutive of Robert. Robert is of Old German origin, meaning "bright fame".'),
    ('Eve', 'Eve is derived from the Hebrew name Hawwa. In Christian belief, Eve was the first woman on Earth.'),
    ('Charlie', 'Charlie is a diminutive form of Charles. Charles has a Germanic origin, meaning "free man".');
