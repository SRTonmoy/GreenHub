from flask import Flask, render_template, request, redirect, url_for, flash, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

user_data = {'email': 'sahriarrahman701@gmail.com', 'password': '41230100828'}

@app.route('/')
def home():
    return render_template('index.html')  # Render login form

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']

    if email == user_data['email'] and password == user_data['password']:
        session['user'] = email  # Store user email in the session
        return redirect(url_for('dashboard'))  # Redirect to the dashboard
    else:
        flash('Invalid email or password', 'error')
        return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return render_template('dashboard.html', user_email=session['user'])  # Pass user's email to the template
    else:
        return redirect(url_for('home'))  # Redirect to login if not logged in

@app.route('/logout')
def logout():
    session.pop('user', None)  # Remove user session
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
