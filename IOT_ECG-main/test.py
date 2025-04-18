import requests
import json
import random
import time

# API endpoint
api_url = 'http://localhost:8000/api/post_data/'

# Function to generate random data
def generate_random_data():
    temperature = round(random.uniform(98.0, 104.0), 2)  # Random temperature between 98.0 and 104.0
    bpm = random.randint(60, 120)  # Random BPM between 60 and 120
    return {"temperature": temperature, "bpm": bpm}

# Number of requests to send
num_requests = 200  # You can adjust this value based on your requirement

# Loop to send POST requests
for _ in range(num_requests):
    data = generate_random_data()

    # Sending POST request
    response = requests.post(api_url, json=data)

    # Print the result
    print(f"Sent data: {data}")
    print(f"Response: {response.status_code} - {response.text}\n")

    # Wait for a short interval (you can adjust this as needed)

