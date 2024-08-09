import http.client
import json

# Create a connection
conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

# Create the headers
headers = {'Content-type': 'application/json'}

# Create the body
body = json.dumps({'title': 'foo', 'body': 'bar', 'userId': 1})

# Send a POST request
conn.request("POST", "/posts", body, headers)

# Get the response
response = conn.getresponse()
print(response.status, response.reason)

data = response.read()
print(data)

# Close the connection
conn.close()
