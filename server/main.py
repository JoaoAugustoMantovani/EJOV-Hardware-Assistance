import os
import flask 
import sqlite3
import login
from flask import Flask, jsonify, request
from flask_cors import CORS

database = sqlite3.connect("ejov-ha.db", timeout=30.00)
cur = database.cursor()

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
