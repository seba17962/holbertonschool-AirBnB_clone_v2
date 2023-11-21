-- Server for the project.
-- hbnb_dev_db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_test_db;
-- Create user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
-- Grant prall privileges
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
-- Gran SELECT privilege on performance_schema.
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
