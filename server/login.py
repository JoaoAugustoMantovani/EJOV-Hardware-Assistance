import os
import flask
import json
import sqlite3
import main
from flask import Flask, jsonify, request
from flask_cors import CORS

database = sqlite3.connect("ejov-ha.db", timeout=30.00)
cur = database.cursor()

app = Flask(__name__)
cors = CORS(app, origins='*')
        
@app.route("/api/user/register", methods=["POST"])
def Register():
    
    data = request.json
    
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    birthdate = data.get('birthdate')
    gender = data.get('gender')
    
    cur.execute(
            "INSERT INTO Users (name, email, password_hash, birthdate, gender) VALUES (?,?,?,?,?)",(
                name, email, password, birthdate, gender
            ))
    database.commit()
    database.close()
    return jsonify({"message": "Registration successful"})
  
@app.route("/api/user/login", methods=["GET"])
def login():
    email = input("Insira Email:")
    password = input("Insira Senha:")

    database.commit()
    database.close()
    return jsonify({})

@app.route("/api/user/changepassword", methods=["POST"])
def changePassword():
    email = input("Insira Email:")

    database.commit()
    database.close()
    return

@app.route("/api/user/deleteuser", methods=["DELETE"])
def deleteUser():
    email = input("Insira Email:")
    password = input("Insira Senha:")

    database.commit()
    database.close()
    return

if __name__ == '__main__':
    app.run(debug=True, port=4000)
