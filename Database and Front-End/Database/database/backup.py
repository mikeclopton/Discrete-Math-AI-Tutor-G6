import shutil
import time

def backup_database(db_name):
    backup_name = f"{db_name}_backup_{int(time.time())}.db"
    shutil.copyfile(db_name, backup_name)
    print(f"Database {db_name} backed up as {backup_name}")

# Example usage
backup_database('users.db')
backup_database('course_progress.db')
