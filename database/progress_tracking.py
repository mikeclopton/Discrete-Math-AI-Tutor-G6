import sqlite3

def create_course_tracking():
    conn = sqlite3.connect('course_progress.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS progress
                      (user_id INTEGER,
                       module_id INTEGER,
                       progress INTEGER,
                       FOREIGN KEY(user_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()

def update_progress(user_id, module_id, progress):
    conn = sqlite3.connect('course_progress.db')
    cursor = conn.cursor()

    cursor.execute('''REPLACE INTO progress (user_id, module_id, progress)
                      VALUES (?, ?, ?)''', (user_id, module_id, progress))

    conn.commit()
    conn.close()

def get_progress(user_id):
    conn = sqlite3.connect('course_progress.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT module_id, progress FROM progress WHERE user_id = ?''', (user_id,))
    progress = cursor.fetchall()

    conn.close()
    return progress

# Example usage
create_course_tracking()
update_progress(1, 101, 50)  # Update progress for user 1, module 101 to 50%
progress = get_progress(1)
print(progress)
