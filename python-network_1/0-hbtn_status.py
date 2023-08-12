import requests

def fetch_hbtn_status():
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)

    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

if __name__ == "__main__":
    fetch_hbtn_status()