-- Table for Football
CREATE TABLE Football (
    P_ID SERIAL PRIMARY KEY,
    P_name VARCHAR(255),
    Size VARCHAR(50),
    Material VARCHAR(50),
    Colour VARCHAR(50),
    Description TEXT,
    Picture VARCHAR(255)
);

-- Table for Football manufacturer
CREATE TABLE Football_Maker (
    M_ID SERIAL PRIMARY KEY,
    M_name VARCHAR(255),
    Address TEXT,
    CNIC VARCHAR(15),
    Contact_no VARCHAR(15),
    Picture VARCHAR(255)
);

-- Table for order history (Football)
CREATE TABLE Football_Order_History (
    P_ID INT REFERENCES Football(P_ID),
    M_ID INT REFERENCES Football_Maker(M_ID),
    Total_Quantity INT,
    Quantity_Delivered INT,
    Quantity_Pending INT GENERATED ALWAYS AS (Total_Quantity - Quantity_Delivered) STORED,
    Price_Per_Item DECIMAL(10,2),
    Total_Price DECIMAL(10,2) GENERATED ALWAYS AS (Quantity_Delivered * Price_Per_Item) STORED
);


--------------------------------------------------------------------------------------------------------------

-- Tables for Gloves
CREATE TABLE Gloves (
    P_ID SERIAL PRIMARY KEY,
    P_name VARCHAR(255),
    Size VARCHAR(50),
    Material VARCHAR(50),
    Colour VARCHAR(50),
    Description TEXT,
    Picture VARCHAR(255)
);

-- Table for Gloves manufacturer
CREATE TABLE Gloves_Maker (
    M_ID SERIAL PRIMARY KEY,
    M_name VARCHAR(255),
    Address TEXT,
    CNIC VARCHAR(15),
    Contact_no VARCHAR(15),
    Picture VARCHAR(255)
);

-- Table for order history (Gloves)
CREATE TABLE Gloves_Order_History (
    P_ID INT REFERENCES Gloves(P_ID),
    M_ID INT REFERENCES Gloves_Maker(M_ID),
    Total_Quantity INT,
    Quantity_Delivered INT,
    Quantity_Pending INT GENERATED ALWAYS AS (Total_Quantity - Quantity_Delivered) STORED,
    Price_Per_Item DECIMAL(10,2),
    Total_Price DECIMAL(10,2) GENERATED ALWAYS AS (Quantity_Delivered * Price_Per_Item) STORED
);
CREATE TABLE users(u_name VARCHAR,u_password VARCHAR);

INSERT INTO users(u_name,u_password) VALUES ('user 1','12345'),('user 2','12345'),('user 3','12345');
CREATE OR REPLACE FUNCTION authenticate_user(u_nam VARCHAR(255), u_pin VARCHAR(255))
RETURNS BOOLEAN AS $$
DECLARE
    user_exists BOOLEAN;
BEGIN
    SELECT EXISTS (
        SELECT 1 FROM users WHERE u_name = authenticate_user.u_nam AND u_password = authenticate_user.u_pin
    ) INTO user_exists;

    RETURN user_exists;
END;
$$ LANGUAGE plpgsql;

SELECT authenticate_user('user 1', '12345');
select * from users;


--inserting some demo data--
INSERT INTO gloves(p_id,p_name,size,material,colour,description) Values (10001,'Working Gloves','L','Soft','Yellow','No Description');
INSERT INTO gloves_maker(m_id,m_name,address,cnic,contact_no) Values (30001,'Ahmed Naeem','House # 274','121323',03203002900);
INSERT INTO gloves_order_history(p_id,m_id,total_quantity,quantity_delivered,price_per_item) VALUES (10001,20001,100,50, 10);

SELECT * FROM gloves_order_history;
SELECT * FROM gloves_maker;
SELECT * FROM gloves;

