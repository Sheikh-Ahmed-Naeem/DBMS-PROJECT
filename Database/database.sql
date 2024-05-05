CREATE DATABASE IF NOT EXISTS Ambassador_Sports_Database;
USE Ambassador_Sports_Database;
CREATE TABLE  Products (
    P_ID INT AUTO_INCREMENT PRIMARY KEY,
    P_name VARCHAR(255),
    Size VARCHAR(50),
    Material VARCHAR(100),
    Colour VARCHAR(50),
    Description TEXT,
    Picture BLOB
);
CREATE TABLE  Maker (
    M_ID INT AUTO_INCREMENT PRIMARY KEY,
    M_name VARCHAR(255),
    Address VARCHAR(255),
    CNIC VARCHAR(15),
    Contact_no VARCHAR(15),
    Picture BLOB
);
CREATE TABLE Order_History (
    P_ID INT,
    M_ID INT,
    Total_Quantity_of_products INT,
    Quantity_Delivered INT,
    Quantity_Pending INT,
    Price_Per_Item DECIMAL(10,2),
    Total_Price DECIMAL(10,2),
    FOREIGN KEY (P_ID) REFERENCES Products(P_ID),
    FOREIGN KEY (M_ID) REFERENCES Maker(M_ID)
);
