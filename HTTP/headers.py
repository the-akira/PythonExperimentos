import requests 

# Requisição para uma API
url = 'https://icanhazdadjoke.com'
response = requests.get(url, headers={'Accept':'application/json'})
data = response.json()
print(data['joke'])