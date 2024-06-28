-- CREATE DATABASE fitness_buddy;

-- USE fitness_buddy;

-- CREATE TABLE Users_Login (
-- user_id INTEGER AUTO_INCREMENT PRIMARY KEY, 
-- user_email VARCHAR(255) NOT NULL, 
-- user_password VARCHAR(255) NOT NULL
-- );


-- INSERT INTO Users_Login (user_email, user_password)
-- VALUES
-- ("bob.belcher@burgershop.com", "IhateSalad987"),
-- ("louise.belcher@gmail.com", "kuchik0pi"),
-- ("tiro@pita.com", "cheesypeeZy*");


SELECT * FROM Users_login WHERE user_email = "tiro@pita.com"  and user_password = "cheesypeeZy*";

