import requests

url = 'https://httpbin.org/get'
headers = {'User-Agent': 'my-app/0.0.1'}
# headers = {'name': 'lucky'}
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())

# Request -- 2 blocks -- Header & Body
