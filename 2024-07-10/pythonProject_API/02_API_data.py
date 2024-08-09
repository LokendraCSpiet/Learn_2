import requests

url = 'https://httpbin.org/post'
data = {'key': 'value'}
response = requests.post(url, data=data)
print(response.status_code)
print(response.json())
