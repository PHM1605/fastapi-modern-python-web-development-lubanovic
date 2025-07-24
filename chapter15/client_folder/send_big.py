import requests
url = "http://localhost:8000/big"
files = {'big_file': open('test_uploaded_file.txt', 'rb')}
resp = requests.post(url, files=files)
print(resp.json()) # file size: 26, name: test_uploaded_file.txt