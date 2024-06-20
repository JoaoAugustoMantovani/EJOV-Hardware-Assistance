import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins='*')

# Mock database for demonstration purposes
users = []


database = sqlite3.connect("ejov-ha.db", check_same_thread=False)
cur = database.cursor()

@app.route('/api/user', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/api/user/register', methods=['POST'])
def register_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    user = {
        'id': len(users) + 1,
        'username': username,
        'password': password  # Note: In a real application, store hashed passwords
    }
    users.append(user)
    return jsonify(user), 201

@app.route('/api/user/login', methods=['POST'])
def login_user():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    
    for user in users:
        if user['username'] == username and user['password'] == password:
            return jsonify({'message': 'Login successful', 'user': user}), 200
    
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route("/api/product/add", methods=["POST"])
def add_product():
    data = request.get_json()
    
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
def update_product():
    data = request.get_json()
    
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
def delete_product():
    data = request.get_json()
    
    product_id = data.get('product_id')
    
    cur.execute("DELETE FROM Products WHERE id=?", (product_id,))
    database.commit()
    return jsonify({"message": "Product deleted successfully"})

@app.route("/api/order/create", methods=["POST"])
def create_order():
    data = request.get_json()
    
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
def update_order():
    data = request.get_json()
    
    order_id = data.get('order_id')
    status = data.get('status')
    
    cur.execute(
        "UPDATE Orders SET status=? WHERE id=?",(
            status, order_id
        ))
    database.commit()
    return jsonify({"message": "Order updated successfully"})

@app.route("/api/order/delete", methods=["DELETE"])
def delete_order():
    data = request.get_json()
    
    order_id = data.get('order_id')
    
    cur.execute("DELETE FROM Orders WHERE id=?", (order_id,))
    database.commit()
    return jsonify({"message": "Order deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True, port=4000)
