CREATE DATABASE IF NOT EXISTS mydatabase;
USE mydatabase;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

INSERT INTO users (name, email) VALUES
  ('Alice', 'alice@test.com'),
  ('Bob', 'bob@test.com');