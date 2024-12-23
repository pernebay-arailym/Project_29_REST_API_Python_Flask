import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes": 78, "name": "Joe", "views": 100000}, 
        {"likes": 10000, "name": "How to make REST API", "views": 80000}, 
        {"likes": 35, "name": "Ary", "views": 2000}]

for i in range(len(data)):
    response = requests.put(BASE + "video/1" + str(i), json=data[i], headers={"Content-Type": "application/json"}) # (calledUrl, headers={"Content-Type": "application/json"}) #wanna send get request to the url
    print(response.json())

input()
response = requests.delete(BASE + "video/0")
print(response)
input()
response = requests.get(BASE + "video/6")
print(response.json())
