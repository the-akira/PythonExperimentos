import requests

response = requests.delete('http://localhost:5000/books/2')

print(response.status_code)