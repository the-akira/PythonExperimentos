import requests
import json

data = {
    'title': 'The Lord of the Rings',
    'genre': 'Fantasy',
    'author_id': 1
}

headers = {'Content-type': 'application/json'}

response = requests.put(
    'http://localhost:5000/books/1',
    data=json.dumps(data), 
    headers=headers
)

print(response.status_code)