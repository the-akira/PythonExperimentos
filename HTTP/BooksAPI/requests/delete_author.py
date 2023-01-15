import requests

response = requests.delete('http://localhost:5000/authors/3')

print(response.status_code)