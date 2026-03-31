import os
import dotenv
from dotenv import load_dotenv
import flask
from flask import Flask, render_template, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
load_dotenv()
app = Flask(__name__)


cred = credentials.Certificate(os.getenv("FIREBASE_CRED_PATH"))
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup")
def account():
    return render_template("auth.html")

@app.route("/auth", methods=["POST", "GET"])
def auth():
    data = request.get_json()
    print("RECEIEVD DATA:", data)
    return jsonify({"status": "success", "received": data})

if __name__ == "__main__":
    app.run(debug=True, port=6969)
    #app.run(host="0.0.0.0", port=5000)