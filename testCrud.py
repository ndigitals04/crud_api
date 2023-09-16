import requests

base = "https://crudapi-7j9x.onrender.com/"
response = requests.put(base + "api", {"user_id":"1", "name":"ndigitals","age":"19","track":"backend"})
print(response.json())
response = requests.put(base + "api", {"user_id":"2", "name":"james","age":"17","track":"youtube"})
print(response.json())
response = requests.get(base + "api/1")
print(response.json())
response = requests.patch(base + "api/4", {"track":"frontend"})
print(response.json())
response = requests.delete(base + "api/1")
print(response)