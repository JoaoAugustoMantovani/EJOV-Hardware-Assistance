from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database for demonstration purposes
users = []

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

if __name__ == '__main__':
    app.run(debug=True)
