import requests

SUPABASE_URL = 'https://lqxupkhygcfnsrlhdyos.supabase.co'
SUPABASE_API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxxeHVwa2h5Z2NmbnNybGhkeW9zIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjU1OTIyMDksImV4cCI6MjA0MTE2ODIwOX0.jjpgiFx8L1b3n_1trErREDg5-sHHMamqcMimrbGxILY'

headers = {
    'apikey': SUPABASE_API_KEY,
    'Authorization': f'Bearer {SUPABASE_API_KEY}',
    'Content-Type': 'application/json',
}

def authenticate_user(email, password):
    url = f"{SUPABASE_URL}/auth/v1/token?grant_type=password"
    payload = {
        'email': email,
        'password': password
    }

    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        print("Authenticated successfully")
        return True
    else:
        print("Authentication failed")
        return False

# Example usage
if authenticate_user('example@example.com', 'password123'):
    print("Login successful")
else:
    print("Login failed")
