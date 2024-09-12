from flask import Flask, render_template, request, redirect, url_for, session
from register import register_user
from auth import authenticate_user
from progress_tracking import get_progress, update_progress, get_user_id
from role_management import change_user_role

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def home():
    return render_template('home.html')

# User Registration Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']
        register_user(email, password, role)  # Calls the Supabase registration API
        return redirect(url_for('login'))
    return render_template('register.html')

# User Login Route
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

# User Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'email' in session:
        email = session['email']
        user_id = get_user_id(email)  # Get user ID from Supabase using the email

        if user_id:
            progress = get_progress(user_id)  # Fetch progress from Supabase
            return render_template('dashboard.html', email=email, progress=progress)
        else:
            return "User not found"
    return redirect(url_for('login'))

# Route to Change User Role
@app.route('/change_role', methods=['POST'])
def change_role():
    if 'email' in session:
        new_role = request.form['role']
        user_id = get_user_id(session['email'])  # Get the user ID from email
        if user_id:
            change_user_role(user_id, new_role)  # Implement user role change in Supabase
            return 'Role updated successfully!'
        else:
            return 'User not found!'
    return redirect(url_for('login'))

# User Logout Route
@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
