from flask import Flask, render_template, request, redirect, url_for, session
from register import register_user
from auth import authenticate_user
from progress_tracking import get_progress, update_progress
from role_management import change_user_role


app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        register_user(username, password, role)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate_user(username, password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        progress = get_progress(1)  # Example user ID
        return render_template('dashboard.html', username=username, progress=progress)
    return redirect(url_for('login'))

@app.route('/change_role', methods=['POST'])
def change_role():
    if 'username' in session:
        new_role = request.form['role']
        change_user_role(session['username'], new_role)
        return 'Role updated successfully!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
