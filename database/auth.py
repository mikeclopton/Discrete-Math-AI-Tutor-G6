from werkzeug.security import check_password_hash
import sqlite3

def authenticate_user(username, password):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT password FROM users WHERE username = ?''', (username,))
    result = cursor.fetchone()

    if result and check_password_hash(result[0], password):
        return True
    return False

# Example usage
if authenticate_user('student2', 'password123'):
    print("Authenticated successfully")
else:
    print("Authentication failed")
