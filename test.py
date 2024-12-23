import requests

BASE = "http://127.0.0.1:5000/"
calledUrl = BASE + "helloworld/bill"
response = requests.get(calledUrl, headers={"Content-Type": "application/json"}) #wanna send get request to the url

try:


    print('whaaat ', response.json())



except requests.exceptions.JSONDecodeError:
    print("Response was not JSON, got:", response)
