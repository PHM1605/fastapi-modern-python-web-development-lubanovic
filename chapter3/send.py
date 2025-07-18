# import requests
# r = requests.get("http://localhost:8000/hi?who=Momfffdsfsdfs")
# print(r.json())

# import httpx
# r = httpx.get("http://localhost:8000/hi")
# print(r.json())

import requests
params = {"who": "Dad"}
# r = requests.get("http://localhost:8000/hi", params=params)
r = requests.post("http://localhost:8000/hi", json={"who":"Dad"})
print(r.json())
