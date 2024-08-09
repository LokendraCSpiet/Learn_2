import requests

url = 'https://httpbin.org/cookies'
cookies = {'session_id': '12345'}
response = requests.get(url, cookies=cookies)
print(response.status_code)
print(response.json())
