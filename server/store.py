import os
import flask
import json
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

# Connect to the database
database = sqlite3.connect("ejov-ha.db", timeout=30.00)
cur = database.cursor()

app = Flask(__name__)
cors = CORS(app, origins='*')

@app.route("/api/product/add", methods=["POST"])
def addProduct():
    data = request.json
    
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    
    cur.execute(
        "INSERT INTO Products (name, description, price, stock) VALUES (?,?,?,?)",(
            name, description, price, stock
        ))
    database.commit()
    return jsonify({"message": "Product added successfully"})

@app.route("/api/product/update", methods=["POST"])
def updateProduct():
    data = request.json
    
    product_id = data.get('product_id')
    name = data.get('name')
    description = data.get('description')
    price = data.get('price')
    stock = data.get('stock')
    
    cur.execute(
        "UPDATE Products SET name=?, description=?, price=?, stock=? WHERE id=?",(
            name, description, price, stock, product_id
        ))
    database.commit()
    return jsonify({"message": "Product updated successfully"})

@app.route("/api/product/delete", methods=["DELETE"])
def deleteProduct():
    data = request.json
    
    product_id = data.get('product_id')
    
    cur.execute("DELETE FROM Products WHERE id=?", (product_id,))
    database.commit()
    return jsonify({"message": "Product deleted successfully"})

@app.route("/api/order/create", methods=["POST"])
def createOrder():
    data = request.json
    
    user_id = data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity')
    
    cur.execute(
        "INSERT INTO Orders (user_id, product_id, quantity) VALUES (?,?,?)",(
            user_id, product_id, quantity
        ))
    database.commit()
    return jsonify({"message": "Order created successfully"})

@app.route("/api/order/update", methods=["POST"])
def updateOrder():
    data = request.json
    
    order_id = data.get('order_id')
    status = data.get('status')
    
    cur.execute(
        "UPDATE Orders SET status=? WHERE id=?",(
            status, order_id
        ))
    database.commit()
    return jsonify({"message": "Order updated successfully"})

@app.route("/api/order/delete", methods=["DELETE"])
def deleteOrder():
    data = request.json
    
    order_id = data.get('order_id')
    
    cur.execute("DELETE FROM Orders WHERE id=?", (order_id,))
    database.commit()
    return jsonify({"message": "Order deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
