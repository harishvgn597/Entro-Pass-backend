from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3
import json

app = Flask(__name__)
CORS(app)


# Define the SQLite database connection
DATABASE = 'entroPass.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# API endpoint to authenticate user
@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        print('hi')
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        username = json_data.get('username')
        password = json_data.get('password')
        print(username,password,'hi')
        # Connect to the database
        conn = get_db_connection()
        c = conn.cursor()

        # Query the Authenticate table for the provided username and password
        c.execute("SELECT * FROM Authenticate WHERE username=? AND password=?", (username, password))
        result = c.fetchone()
        
        # Close the database connection
        conn.close()
        print(result)
        # Check if the result is not None (i.e., username and password found)
        if result:
            response_data = {'authenticated': True, 'message': 'User authenticated successfully'}
        else:
            response_data = {'authenticated': False, 'message': 'Invalid username or password'}

        # Return the response data as JSON
        return jsonify(response_data)
    
@app.route('/signUp', methods=['POST'])
def signUp():
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        json_data = json.loads(data)
        username = json_data.get('username')
        password = json_data.get('password')
        
        # Connect to the database
        conn = get_db_connection()
        c = conn.cursor()

        # Insert the new username and password into the Authenticate table
        try:
            c.execute("INSERT INTO Authenticate (username, password) VALUES (?, ?)", (username, password))
            conn.commit()
            response_data = {'success': True, 'message': 'User registered successfully'}
        except sqlite3.IntegrityError:
            # Handle case where username is already in use
            response_data = {'success': False, 'message': 'Username already exists'}

        # Close the database connection
        conn.close()

        # Return the response data as JSON
        return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)

