import requests

BASE_URL = "http://localhost:8000"

def test_recognize_input():
    url = f"{BASE_URL}/recognize_input"
    data = {
        "content": "2x + 3 = 7",
        "input_type": "latex"
    }
    response = requests.post(url, json=data)
    print("Recognize Input Response:", response.status_code)
    print("Response content:", response.text)
    print("Response headers:", response.headers)

def test_generate_response():
    url = f"{BASE_URL}/generate_response"
    data = {
        "question": "Solve 2x + 3 = 7"
    }
    response = requests.post(url, json=data)
    print("Generate Response Response:", response.status_code)
    print("Response content:", response.text)
    print("Response headers:", response.headers)

if __name__ == "__main__":
    test_recognize_input()
    print("\n")
    test_generate_response()