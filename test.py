import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld") #wanna send get request to the url
print(response.json())