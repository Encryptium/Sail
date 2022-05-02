from flask import Flask, render_template, request, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Create the application instance
app = Flask(__name__, template_folder='templates')
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = os.environ['SECRET_KEY']

# Index Page
@app.route('/')
def index():
    # If the user is not logged in, redirect to the login page
    if 'logged_in' not in session:
        return redirect('/login')
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    # If the user is already logged in, redirect to the main page
    if 'logged_in' in session:
        return redirect('/')
    return render_template('login.html')

# Register Page
@app.route('/register')
def register():
    # If the user is already logged in, redirect to the main page
    if 'logged_in' in session: 
        return redirect('/')
    return render_template('register.html')

# start server on host 0.0.0.0 and port 8080
app.run(host='0.0.0.0', port=8080, debug=True)
