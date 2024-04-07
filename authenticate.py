from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True, origins='https://cors-anywhere.herokuapp.com')

@app.route('/authenticate', methods=['POST'])
def authenticate_user():
    data = request.get_json()
    username = data['username']
    password = data['password']

    # Your authentication logic here

    # For demonstration purposes, we'll simply check if the username and password match
    if username == 'example_user' and password == 'example_password':
        return jsonify({'authenticated': True, 'message': 'User authenticated successfully'})
    else:
        return jsonify({'authenticated': False, 'message': 'Invalid username or password'})

if __name__ == '__main__':
    app.run(debug=True)
