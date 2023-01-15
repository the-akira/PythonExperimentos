import requests
import json

data = {
    'title': 'The Lord of the Rings',
    'genre': 'Fantasy',
    'author_id': 3
}

headers = {'Content-type': 'application/json'}

response = requests.put(
    'http://localhost:5000/books/2', 
    data=json.dumps(data), 
    headers=headers
)

print(response.status_code)