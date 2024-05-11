from flask import Flask, render_template,request
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
    return render_template('Gloves_product_window.html')


@app.route('/gloves/makers')
def gloves_makers():
    return render_template('G_maker_window.html')


@app.route('/order_history')
def order_history():
    return render_template('order_history.html')


@app.route('/football/products')
def football_products():
    return render_template('products_page.html')


@app.route('/football/makers')
def football_makers():
    return render_template('makers_page.html')


@app.route('/football/order_history')
def football_order_history():
    return render_template('order_history_page.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    connect()
