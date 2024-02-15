import requests

BASE = "http://127.0.0.1:5000/"
response = requests.get(BASE + "video/5")
print(response.json())

response = requests.put(BASE + "video/5",{"likes":10, "name":"tim","views":10000})
print(response.json())

response = requests.get(BASE + "video/5")
print(response.json())

response = requests.patch(BASE + "video/5",{"likes":16, "name":"tim","views":100})
print(response.json())

response = requests.get(BASE + "video/5")
print(response.json())

response = requests.delete(BASE + "video/5")
print(response.json())