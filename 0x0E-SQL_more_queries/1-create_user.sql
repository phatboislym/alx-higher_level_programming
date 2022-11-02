-- creates the user user_0d_1 with all privileges
-- the user_0d_1 password should be set to user_0d_1_pwd
-- if the user_0d_1 already exists, the script should not fail
CREATE USER
    IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES
   ON *.*
   TO 'user_0d_1'@'localhost'
   IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
