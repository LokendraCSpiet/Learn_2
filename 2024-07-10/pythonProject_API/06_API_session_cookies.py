import requests

session = requests.Session()
session.get('https://httpbin.org/cookies/set/sessioncookie/123456789')
response = session.get('https://httpbin.org/cookies')
print(response.status_code)
print(response.json())
