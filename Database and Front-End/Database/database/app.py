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
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        register_user(email, password, role)
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if authenticate_user(email, password):
            session['email'] = email
            return redirect(url_for('dashboard'))
        else:
            return 'Login Failed'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        email = session['email']
        progress = get_progress('user_id')  # Placeholder, implement user ID retrieval
        return render_template('dashboard.html', email=email, progress=progress)
    return redirect(url_for('login'))

@app.route('/change_role', methods=['POST'])
def change_role():
    if 'email' in session:
        new_role = request.form['role']
        change_user_role(session['user_id'], new_role)  # Implement user ID retrieval
        return 'Role updated successfully!'
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
