import requests

SUPABASE_URL = 'https://lqxupkhygcfnsrlhdyos.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxxeHVwa2h5Z2NmbnNybGhkeW9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1OTIyMDksImV4cCI6MjA0MTE2ODIwOX0.jjpgiFx8L1b3n_1trErREDg5-sHHMamqcMimrbGxILY'

headers = {
    'apikey': SUPABASE_API_KEY,
    'Authorization': f'Bearer {SUPABASE_API_KEY}',
    'Content-Type': 'application/json',
}

def change_user_role(user_id, new_role):
    url = f"{SUPABASE_URL}/rest/v1/roles"
    payload = {
        'user_id': user_id,
        'role': new_role
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Role updated for user {user_id}")
    else:
        print("Error updating role:", response.json())

# Example usage
change_user_role('user_id_123', 'educator')
