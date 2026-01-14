CREATE DATABASE user_management;

USE user_management;

CREATE TABLE user_details (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    gender VARCHAR(20),
    phone VARCHAR(20),
    place VARCHAR(100),
    age INT
);
