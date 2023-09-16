import requests

base = "http://127.0.0.1:5000/"
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