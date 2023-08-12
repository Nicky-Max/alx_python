"""
Sends a request to a URL and displays the value of the X-Request-Id header in the response.
"""

import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Get the value of the X-Request-Id header from the response
    x_request_id = response.headers.get('X-Request-Id')
    
    if x_request_id:
        print(x_request_id)

if __name__ == "__main__":
    main()