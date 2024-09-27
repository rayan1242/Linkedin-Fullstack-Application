-- CREATE DATABASE linkedin;
-- use linkedin;
-- CREATE TABLE user (
--     user_id INT PRIMARY KEY AUTO_INCREMENT,
--     name VARCHAR(100) NOT NULL,
--     dob DATE NOT NULL,
--     age INT,
--     profile_pic VARCHAR(255),
--     location_city VARCHAR(50) NOT NULL,
--     location_state VARCHAR(50) NOT NULL,
--     location_country VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE institution (
--     institution_id INT PRIMARY KEY AUTO_INCREMENT,
--     no_of_employees INT NOT NULL,
--     website VARCHAR(255) NOT NULL,
--     industry VARCHAR(50) NOT NULL,
--     name VARCHAR(50) NOT NULL,
--     description VARCHAR(255) NOT NULL,
--     location_city VARCHAR(50) NOT NULL,
--     location_state VARCHAR(50) NOT NULL,
--     location_country VARCHAR(50) NOT NULL
-- );

-- CREATE TABLE experience (
--     exp_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     institution_id INT NOT NULL,
--     start DATE NOT NULL,
--     end DATE NOT NULL,
--     description VARCHAR(255) NOT NULL,
--     title VARCHAR(50) NOT NULL,
--     duration INT AS (DATEDIFF(end, start)) VIRTUAL,
--     FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
--     FOREIGN KEY (institution_id) REFERENCES institution(institution_id)
-- );

-- CREATE TABLE education (
--     edu_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     institution_id INT NOT NULL,
--     start DATE NOT NULL,
--     end DATE NOT NULL,
--     course VARCHAR(50) NOT NULL,
--     duration INT AS (DATEDIFF(end, start)) VIRTUAL,
--     FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
--     FOREIGN KEY (institution_id) REFERENCES institution(institution_id)
-- );

-- CREATE TABLE job (
--     job_id INT PRIMARY KEY AUTO_INCREMENT,
--     institution_id INT NOT NULL,
--     job_title VARCHAR(50) NOT NULL,
--     description VARCHAR(255) NOT NULL,
--     type VARCHAR(50) NOT NULL,
--     FOREIGN KEY (institution_id) REFERENCES institution(institution_id) ON DELETE CASCADE
-- );

-- CREATE TABLE application (
--     application_id INT PRIMARY KEY AUTO_INCREMENT,
--     job_id INT NOT NULL,
--     user_id INT NOT NULL,
--     application_status VARCHAR(50) NOT NULL,
--     application_date DATE NOT NULL,
--     FOREIGN KEY (job_id) REFERENCES job(job_id),
--     FOREIGN KEY (user_id) REFERENCES user(user_id)
-- );

-- CREATE TABLE linkedin.connection (
--     connection_id INT PRIMARY KEY AUTO_INCREMENT,
--     userIdA INT NOT NULL,
--     userIdB INT NOT NULL,
--     connection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
--     FOREIGN KEY (userIdA) REFERENCES user(user_id) ON DELETE CASCADE,
--     FOREIGN KEY (userIdB) REFERENCES user(user_id) ON DELETE CASCADE,
--     CHECK (userIdA < userIdB),
--     UNIQUE(userIdA, userIdB)
-- );

-- CREATE TABLE phone_no (
--     phone_id INT PRIMARY KEY AUTO_INCREMENT,
--     user_id INT NOT NULL,
--     phone_number VARCHAR(50) NOT NULL,
--     FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE
-- );

-- CREATE TABLE post (
--     post_id INT AUTO_INCREMENT,
--     user_id INT,
--     post_content TEXT NOT NULL,
--     post_date DATETIME DEFAULT CURRENT_TIMESTAMP,
--     PRIMARY KEY (post_id, user_id),
--     CONSTRAINT fk_user
--         FOREIGN KEY (user_id)
--         REFERENCES user(user_id)
--         ON DELETE CASCADE
-- );

-- CREATE TABLE skill (
--     skill_id INT PRIMARY KEY AUTO_INCREMENT,
--     skill_name VARCHAR(50) NOT NULL
-- );

CREATE TABLE user_skill(
	-- user_skill_id INT PRIMARY KEY AUTO_INCREMENT,
    skill_id INT NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(user_id) ON DELETE CASCADE,
    FOREIGN KEY (skill_id) REFERENCES skill(skill_id) ON DELETE CASCADE,
    PRIMARY KEY (skill_id, user_id)
);

















