<div align="center">

# Inventory Management System 📦💻

<br>

<p align="center">

  <h2><strong>This project is an inventory management system built for a factory.</strong></h2>

</p>

</div>


<br>


## Description ℹ️

The Inventory Management System allows users to manage products, manufacturers, and order history efficiently. It provides functionalities like adding new products, deleting existing products, viewing product details, and checking order history.

## Framework and Dependencies 🛠️

This project is built using the Flask framework, a lightweight WSGI web application framework in Python. It utilizes the following dependencies:

- Flask
  ```bash
   pip install flask
  ```
- psycopg
  ```bash
  pip3 install psycopg2
  ```

## How to Run ▶️

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/B3TA-BLOCKER/DBMS-PROJECT.git
    ```

2. **Database Setup:**

    - Set up a PostgreSQL database.
  
      - **config.py**: This file contains configurations for the project. Make sure to update it with the appropriate settings for your environment.

      - **database.ini**: This file contains the database connection settings. Ensure that it is correctly configured with the details of your PostgreSQL database.

      - Use the provided `database_structure.sql` file to create the required tables and schema in your database.

3. **Run the Application:**

    ```bash
    python app.py
    ```

4. **Access the Application:**

    Open your web browser and navigate to `http://localhost:5000` to access the application.

## Note 📝

Since the application is running on localhost, make sure your local server is running to access it.

## Contributors 👥

- **Hassaan Ali Bukhari:** Backend development, HTML login page, CSS modifications, HTML file connections.
- **Ammaid:** Database design and setup, prototype creation using Figma, data insertion.
- **Ahmad Naeem:** Basic HTML page creation, documentation.

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
