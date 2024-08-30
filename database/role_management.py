import sqlite3

def change_user_role(username, new_role):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''UPDATE users SET role = ? WHERE username = ?''', (new_role, username))

    conn.commit()
    conn.close()

# Example usage
change_user_role('student1', 'educator')
