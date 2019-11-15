import requests

res = requests.get('https://news.ycombinator.com/')
# print(res.ok)
# print(res.headers)
# print(res.text)

url = 'http://www.google.com'
response = requests.get(url)
print(f'sua requisição para {url} tem o status {response.status_code}')