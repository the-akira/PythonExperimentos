import requests

response = requests.delete('http://localhost:5000/authors/1')

print(response.status_code)