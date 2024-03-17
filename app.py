from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

# Mock database for user authentication (replace with actual database in production)
users = {
    "user1": {"password": "password1", "fullname": "User One"},
    "user2": {"password": "password2", "fullname": "User Two"}
}

# Define routes for different pages
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]['password'] == password:
            # Successful login
            return redirect(url_for('dashboard'))
        else:
            # Failed login
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Mock user session (replace with actual user session handling)
    username = "user1"  # Example: Retrieve username from session
    if username:
        fullname = users[username]['fullname']
        return render_template('dashboard.html', fullname=fullname)
    else:
        return redirect(url_for('login'))

@app.route('/schedule')
def schedule():
    # Mock user session (replace with actual user session handling)
    username = "user1"  # Example: Retrieve username from session
    if username:
        return render_template('schedule.html')
    else:
        return redirect(url_for('login'))

@app.route('/consultation')
def consultation():
    # Mock user session (replace with actual user session handling)
    username = "user1"  # Example: Retrieve username from session
    if username:
        return render_template('consultation.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
