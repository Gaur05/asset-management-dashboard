DROP TABLE IF EXISTS user_details;


CREATE TABLE user_details (

    id SERIAL PRIMARY KEY,

    name VARCHAR(100),

    user_id VARCHAR(100) UNIQUE,

    email VARCHAR(100) UNIQUE,

    password VARCHAR(100)

);


-- SELECT * FROM user_details;