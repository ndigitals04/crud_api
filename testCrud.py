import requests

base = "https://e494-105-113-33-134.ngrok-free.app/"
response = requests.put(base + "api", {"user_id":"5", "name":"ndu","age":"19","track":"band"})
print(response.json())
response = requests.put(base + "api", { "name":"tutu"})
print(response.json())
response = requests.get(base + "api/tutu")
print(response.json())
response = requests.patch(base + "api/ndu", {"name":"jane"})
print(response.json())
response = requests.delete(base + "api/1")
print(response)