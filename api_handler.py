import os  # Import the os module to interact with the operating system environment
import requests  # Import the requests module to make HTTP requests

# Retrieve the API token from an environment variable named 'HF_TOKEN'
API_TOKEN = os.environ["HF_TOKEN"] # Set a API_TOKEN environment variable before running

# Retrieve the API endpoint URL from an environment variable named 'HF_ENDPOINT'
API_URL = os.environ["HF_ENDPOINT"] # Add a URL for a model of your choosing

# Prepare the headers for the HTTP request, including the Authorization token
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Define a function named 'query' that takes a prompt as an argument
def query(prompt):
    # Define the payload (data) to be sent in the HTTP request
    payload = {
        "inputs": prompt,
        "parameters": {  # Additional parameters for the API request
            "max_new_tokens": 500,  # Maximum number of new tokens to generate
            "temperature": 0.5,  # Controls randomness in generation, lower is more deterministic
            "top_p": 0.84,  # Nucleus sampling: higher value means more diversity
            "do_sample": False,  # If True, sampling is used for generation, otherwise greedy approach
            "return_full_text": False  # If False, only the generated text is returned
        }
    }
    # Make a POST request to the API URL with the headers and payload, and get the response
    response = requests.post(API_URL, headers=headers, json=payload)
    # Extract and return the generated text from the response
    # Check if the response is successful
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        return "There was an error processing your request."

    # Try to extract the generated text
    try:
        res = response.json()[0]['generated_text']
        print("RES =========================================")
        print(res)
        return res
    except (IndexError, KeyError, TypeError):
        print("Error: Unable to extract 'generated_text' from the response.")
        return "There was an error extracting the response."

