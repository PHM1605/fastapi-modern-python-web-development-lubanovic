import requests
r = requests.get("http://localhost:8000/who", auth=("me", "secret"))
print(r.json())