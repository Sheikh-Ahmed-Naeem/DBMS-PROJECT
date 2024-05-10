from pyrebase import * 
from flask import *


app = Flask(__name__)

firebaseConfig = {
    "apiKey": "AIzaSyDD_5YYw-MdkABvEvobj-N5qzNhRla7gFY",
    "authDomain": "ambassador-sports.firebaseapp.com",
    "projectId": "ambassador-sports",
    "storageBucket": "ambassador-sports.appspot.com",
    "messagingSenderId": "591659592990",
    "appId": "1:591659592990:web:14f45c65b77efc1e6aed0f",
    "measurementId": "G-PMNMYH39PC",
    "databaseURL": "https://ambassador-sports-default-rtdb.asia-southeast1.firebasedatabase.app/"
}

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

@app.route("/test",methods=["GET"])
def test():
    print('This is a test')


@app.route('/insert_maker',methods=['POST'])
def insert_maker():
    data = request.json
    makername = data['maker_name']
    makerphone = data["maker_phone"]
    makercnic = data["maker_cnic"]
    makeraddress = data["maker_address"]
    makerpic = data["maker_pic"]

    db.child(makerphone).set(data)



@app.route('/select_maker',methods=['POST'])
def select_maker():
    data = db.get().val()

    return jsonify(data)



if __name__ == "__main__":
    app.run("0.0.0.0",port=4444)