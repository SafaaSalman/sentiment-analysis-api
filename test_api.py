import requests
import json

BASE_URL = "http://localhost:8000"

def run_tests():
    print("Testing API endpoints...\n")
    
    # Health check endpoint
    print("1. Testing health check:")
    response = requests.get(f"{BASE_URL}/health")
    print_response(response)
    
    # Positive sentiment test
    print("\n2. Testing positive sentiment:")
    response = requests.post(
        f"{BASE_URL}/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": "I really enjoyed this movie!"})
    )
    print_response(response)
    
    # Negative sentiment test
    print("\n3. Testing negative sentiment:")
    response = requests.post(
        f"{BASE_URL}/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": "I hated the terrible acting in this film."})
    )
    print_response(response)
    
    # Neutral sentiment test
    print("\n4. Testing neutral sentiment:")
    response = requests.post(
        f"{BASE_URL}/predict",
        headers={"Content-Type": "application/json"},
        data=json.dumps({"text": "The movie was okay, nothing special."})
    )
    print_response(response)
    
    # Empty text test
    print("\n5. Testing empty text:")
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps({"text": ""})
        )
        print_response(response)
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print("Response Body:")
        print(json.dumps(response.json(), indent=2))
    except ValueError:
        print("Response text:", response.text)

if __name__ == "__main__":
    run_tests()