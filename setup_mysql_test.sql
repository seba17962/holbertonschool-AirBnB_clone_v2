-- Task 4
-- script that prepares a MySQL server for the project
CREATE database if not exists hbnb_test_db;
USE hbnb_test_db;
CREATE user if not exists 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT PRIVILEGES ON performance_schema.* TO 'hbnb_test'@'localhost'
