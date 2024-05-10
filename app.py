from flask import Flask, render_template

app = Flask(__name__)


# routing the application
@app.route("/")
def application():
  return render_template('login.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
