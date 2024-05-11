from flask import Flask, render_template, request, redirect, url_for
import psycopg2
from config import config

app = Flask(__name__)


def connect():
    connection = None
    try:
        params = config()
        connection = psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()


# routing the application
@app.route("/")
def application():
    return render_template('login.html')


def check_credentials(username, password):
    try:
        # Get database connection settings from database.ini
        params = config()

        # Connect to the database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Query the database to check if the credentials are valid
        cursor.execute("SELECT * FROM users WHERE  u_name = %s AND  u_password = %s", (username, password))
        user = cursor.fetchone()

        # Close database connection
        cursor.close()
        conn.close()

        return user is not None  # Return True if user exists, False otherwise

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error connecting to the database:", e)
        return False


def fetch_data_Gloves():
    try:
        # Get database connection settings from database.ini
        params = config()

        # Connect to the database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Query the database to fetch all rows from the Gloves_Maker table
        cursor.execute("SELECT * FROM Gloves")

        # Fetch all rows and store them in a list of dictionaries
        products = []
        for row in cursor.fetchall():
            maker = {
                'name': row[0], 
                'unit_address': row[1],  
                'contact_no': row[2] 
            }
            products.append(maker)

        # Close database connection
        cursor.close()
        conn.close()

        return products

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error connecting to the database:", e)
        return None


def fetch_data():
    try:
        # Get database connection settings from database.ini
        params = config()

        # Connect to the database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Query the database to fetch all rows from the Gloves_Maker table
        cursor.execute("SELECT * FROM Gloves_Maker")
        makers = []
        for row in cursor.fetchall():
            maker = {
                'name': row[1], 
                'unit_address': row[2],  
                'contact_no': row[4]  
            }
            makers.append(maker)

        # Close database connection
        cursor.close()
        conn.close()

        return makers

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error connecting to the database:", e)
        return None


def product_fetch_data():
    try:
        # Get database connection settings from database.ini
        params = config()

        # Connect to the database
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()

        # Query the database to fetch all rows from the Gloves_Maker table
        cursor.execute("SELECT * FROM Gloves")
        details = cursor.fetchall()
        cursor.close()
        conn.close()
        
        print(details[0])
        return details

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error connecting to the database:", e)
        return None


def insert_product(product_name, size, material, colour, description):
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()
        cursor.execute("INSERT INTO Gloves (P_name, Size, Material, Colour, Description) VALUES (%s, %s, %s, %s, %s)",
                       (product_name, size, material, colour, description))
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        cursor.close()
        conn.close()


# Function to delete an item from the database
def delete_item_from_database(item_id):
    try:
        params = config()
        conn = psycopg2.connect(**params)

        cursor = conn.cursor()
        cursor.execute("DELETE FROM Gloves WHERE P_ID = %s", (item_id,))
        conn.commit()

    except (Exception, psycopg2.DatabaseError) as e:
        print("Error deleting item from the database:", e)
    finally:
        cursor.close()
        conn.close()


@app.route('/Home_Page', methods=['POST'])
def button_click():
    username = request.form['u']
    password = request.form['p']

    if check_credentials(username, password):
        return render_template('index.html')
    else:
        return "Invalid credentials.", 400


@app.route('/gloves/products')
def gloves_products():
    data = fetch_data_Gloves()
    return render_template('Gloves_product_window.html', products=data)


@app.route('/Add_Product.html')
def add_product():
    return render_template('Add_Product.html')


@app.route('/gloves/products', methods=['POST'])
def save_product():
    if request.method == 'POST':
        # Retrieve form data
        product_name = request.form['product_name']
        product_id = request.form['product_id']
        maker = request.form['maker']
        material = request.form['material']
        colour = request.form['colour']

        insert_product(product_name, product_id, maker, material, colour)

        return redirect(url_for('gloves_products'))


@app.route('/Delete_Product.html')
def delete_product():
    data = product_fetch_data()
    return render_template('Delete_Product.html', Gloves=data)


@app.route('/delete_item', methods=['POST','GET'])
def delete_item():
    if request.method == 'POST':
        item_id = request.form['delete_item']
        print(item_id)
        delete_item_from_database(item_id)  # Call the function to delete the item from the database
        return redirect(url_for('gloves_products'))  # Redirect to the Gloves_product_window.html page


@app.route('/gloves/makers')
def gloves_makers():
    data = fetch_data()
    return render_template('Gloves_maker_window.html', makers=data)


@app.route('/order_history')
def order_history():
    data = fetch_order_history_data()  
    return render_template('Gloves_Order_History.html', order_history_data=data)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    connect()
