import requests
url = "http://localhost:8000/small"
files = {'small_file': open('test_uploaded_file.txt', 'rb')}
resp = requests.post(url, files=files)
print(resp.json())
