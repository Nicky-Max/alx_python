"""
Sends a POST request to a URL with an email as a parameter and displays the response body.
"""

import requests
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Data to be sent in the POST request
    data = {'email': email}
    
    # Send a POST request to the URL with the data
    response = requests.post(url, data=data)
    
    # Display the response body
    print(response.text)

if __name__ == "__main__":
    main()