import requests
import json

data = {
    'title': 'The Hobbit',
    'genre': 'Novel',
    'author_id': 1
}

headers = {'Content-type': 'application/json'}

response = requests.post(
    'http://localhost:5000/books', 
    data=json.dumps(data), 
    headers=headers
)

print(response.status_code)