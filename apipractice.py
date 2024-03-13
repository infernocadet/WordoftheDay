import requests

# Use httpbin for demonstration
url = "https://httpbin.org/json"

# Make a GET request to the URL
response = requests.get(url)

# Check if request was successfu.
if response.status_code == 200:
    # convert response to JSON format
    data = response.json()
    print("API call successful. Received data:")
    print(data)
else:
    print("Failed to fetch data from API.")