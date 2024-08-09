import requests

url = 'https://httpbin.org/delay/5'
try:
    response = requests.get(url, timeout=3)
except requests.Timeout:
    print('The request timed out')
