CREATE TABLE assets (

    id SERIAL PRIMARY KEY,

    asset_name VARCHAR(100),

    category VARCHAR(50),

    status VARCHAR(30),

    assigned_to VARCHAR(100),

    asset_value DECIMAL(10,2)

);


SELECT * FROM assets;