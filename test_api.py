import requests
import json

API_URL = "http://localhost:5000"

def test_health():
    response = requests.get(f"{API_URL}/health")
    print(f"Health Check: {response.status_code} - {response.json()}")

def test_prediction(text):
    data = {"text": text}
    response = requests.post(f"{API_URL}/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        print(f"Text: '{text}'")
        print(f"Prediction: {result['label']} (Confidence: {result['confidence']})")
        print("-" * 50)
    else:
        print(f"Error: {response.status_code} - {response.text}")

def main():
    print("Testing Reply Classification API")
    print("=" * 50)

    test_health()
    print()

    test_cases = [
        "I'm excited to see the demo!",
        "Not interested, please remove me from your list",
        "Can you send me pricing details?",
        "Let's schedule a meeting next week",
        "This doesn't fit our current needs",
        "I'll need to discuss this with my team"
    ]

    for test_case in test_cases:
        test_prediction(test_case)

if __name__ == "__main__":
    main()
