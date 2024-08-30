from werkzeug.security import generate_password_hash
import sqlite3

def register_user(username, password, role='student'):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      username TEXT UNIQUE NOT NULL,
                      password TEXT NOT NULL,
                      role TEXT NOT NULL)''')

    # Check if the username already exists
    cursor.execute('''SELECT * FROM users WHERE username = ?''', (username,))
    if cursor.fetchone():
        print(f"Username '{username}' already exists. Please choose a different username.")
        conn.close()
        return

    # Hash the password
    hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
    
    # Insert the new user
    cursor.execute('''INSERT INTO users (username, password, role)
                      VALUES (?, ?, ?)''', (username, hashed_password, role))

    conn.commit()
    conn.close()
    print(f"User '{username}' registered successfully.")

# Example usage
register_user('student2', 'password123', 'student')
