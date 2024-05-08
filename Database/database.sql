
CREATE DATABASE Ambassador_Sports;
USE Ambassador_Sports;

-- table for Football
CREATE TABLE Football (
    P_ID INT AUTO_INCREMENT PRIMARY KEY,
    P_name VARCHAR(255),
    Size VARCHAR(50),
    Material VARCHAR(50),
    Colour VARCHAR(50),
    Description TEXT,
    Picture VARCHAR(255)
);

-- tabke for Football manufacturer
CREATE TABLE Football_Maker (
    M_ID INT AUTO_INCREMENT PRIMARY KEY,
    M_name VARCHAR(255),
    Address TEXT,
    CNIC VARCHAR(15),
    Contact_no VARCHAR(15),
    Picture VARCHAR(255)
);

-- table for order history (Football)
CREATE TABLE Football_Order_History (
    P_ID INT,
    M_ID INT,
    Total_Quantity INT,
    Quantity_Delivered INT,
    Quantity_Pending INT GENERATED ALWAYS AS (Total_Quantity - Quantity_Delivered) VIRTUAL,
    Price_Per_Item DECIMAL(10,2),
    Total_Price DECIMAL(10,2) GENERATED ALWAYS AS (Quantity_Delivered * Price_Per_Item) VIRTUAL,
    FOREIGN KEY (P_ID) REFERENCES Football (P_ID),
    FOREIGN KEY (M_ID) REFERENCES Football_Maker (M_ID)
);

--------------------------------------------------------------------------------------------------------------
 -- tables are used for Gloves--

CREATE TABLE Gloves (
    P_ID INT AUTO_INCREMENT PRIMARY KEY,
    P_name VARCHAR(255),
    Size VARCHAR(50),
    Material VARCHAR(50),
    Colour VARCHAR(50),
    Description TEXT,
    Picture VARCHAR(255)
);

-- table for Gloves manufacturer
CREATE TABLE Gloves_Maker (
    M_ID INT AUTO_INCREMENT PRIMARY KEY,
    M_name VARCHAR(255),
    Address TEXT,
    CNIC VARCHAR(15),
    Contact_no VARCHAR(15),
    Picture VARCHAR(255)
);

-- table for order history (Gloves)
CREATE Gloves_Order_History (
    P_ID INT,
    M_ID INT,
    Total_Quantity INT,
    Quantity_Delivered INT,
    Quantity_Pending INT GENERATED ALWAYS AS (Total_Quantity - Quantity_Delivered) VIRTUAL,
    Price_Per_Item DECIMAL(10,2),
    Total_Price DECIMAL(10,2) GENERATED ALWAYS AS (Quantity_Delivered * Price_Per_Item) VIRTUAL,
    FOREIGN KEY (P_ID) REFERENCES Gloves (P_ID),
    FOREIGN KEY (M_ID) REFERENCES Gloves_Maker (M_ID)
);

