import requests
import json

data = {
    'name': 'Tolkien'
}
headers = {'Content-type': 'application/json'}

response = requests.put(
    'http://localhost:5000/authors/3', 
    data=json.dumps(data), 
    headers=headers
)

print(response.status_code)