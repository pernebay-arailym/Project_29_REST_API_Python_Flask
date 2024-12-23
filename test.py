import requests

BASE = "http://127.0.0.1:5000/"
#calledUrl = BASE + "video/1", {"likes": 10}
response = requests.put(BASE + "video/1", json={"likes": 10, "name": "Ary", "views": 100000}) # (calledUrl, headers={"Content-Type": "application/json"}) #wanna send get request to the url
#try:
print(response.json())
input()
response = requests.get(BASE + "video/1")
print(response.json())


#except requests.exceptions.JSONDecodeError:
    #print("Response was not JSON, got:", response)
