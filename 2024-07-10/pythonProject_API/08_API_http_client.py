import http.client

# Create a connection

conn = http.client.HTTPSConnection("www.example.com")

# Send a GET request
conn.request("GET", "/")

# Get the response
response = conn.getresponse()

# Print the status and response
print(response.status, response.reason)
data = response.read()
print(data)

# Close the connection
conn.close()
