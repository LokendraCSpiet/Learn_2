import requests
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[
                        logging.FileHandler("api_requests.log"),
                        logging.StreamHandler()
                    ])


def log_request_response(func):
    def wrapper(*args, **kwargs):
        logging.debug(f"Request: {args}, {kwargs}")
        response = func(*args, **kwargs)
        logging.debug(f"Response: (response.status_code), (response.text)")
        return response
    return wrapper


# Wrap the requests methods with the logging function
requests.get = log_request_response(requests.get)
requests.post = log_request_response(requests.post)
requests.put = log_request_response(requests.put)
requests.delete = log_request_response(requests.delete)

# Example usage
response = requests.get('https://httpbin.org/get')
print(response.status_code)
response = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(response.status_code)