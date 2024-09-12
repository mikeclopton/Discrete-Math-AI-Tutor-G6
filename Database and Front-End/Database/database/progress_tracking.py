import requests

SUPABASE_URL = 'https://lqxupkhygcfnsrlhdyos.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxxeHVwa2h5Z2NmbnNybGhkeW9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1OTIyMDksImV4cCI6MjA0MTE2ODIwOX0.jjpgiFx8L1b3n_1trErREDg5-sHHMamqcMimrbGxILY'

headers = {
    'apikey': SUPABASE_API_KEY,
    'Authorization': f'Bearer {SUPABASE_API_KEY}',
    'Content-Type': 'application/json',
}

# Get user ID based on the email address
def get_user_id(email):
    url = f"{SUPABASE_URL}/rest/v1/users?email=eq.{email}&select=id"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        if user_data:
            return user_data[0]['id']  # Assuming email is unique and we return the user ID
        else:
            return None
    else:
        print(f"Error fetching user ID: {response.json()}")
        return None

# Fetch user progress by user_id
def get_progress(user_id):
    url = f"{SUPABASE_URL}/rest/v1/progress?user_id=eq.{user_id}&select=module_id,progress"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        progress_data = response.json()
        return progress_data  # Returns progress data as a list of dictionaries
    else:
        print(f"Error fetching progress: {response.json()}")
        return None

# Update user progress
def update_progress(user_id, module_id, progress):
    url = f"{SUPABASE_URL}/rest/v1/progress"
    payload = {
        'user_id': user_id,
        'module_id': module_id,
        'progress': progress
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Progress updated for user {user_id}, module {module_id}")
    else:
        print("Error updating progress:", response.json())
