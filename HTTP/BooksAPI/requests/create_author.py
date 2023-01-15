import requests
import json

data = {
    'name': 'J.R.R Tolkien'
}

headers = {'Content-type': 'application/json'}

response = requests.post(
    'http://localhost:5000/authors', 
    data=json.dumps(data), 
    headers=headers
)

print(response.status_code)