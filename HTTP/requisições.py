import requests

# Fazendo uma requisição HTTP
resposta = requests.get('https://cc33z.netlify.app')
# Resposta está OK?
print(resposta.ok)
# Cabeçalhos
print(resposta.headers)
# Conteúdo HTML
print(resposta.text)

# Fazendo outra requisição HTTP
url = 'http://www.google.com'
response = requests.get(url)
print(f'Sua requisição para {url} tem o status: {response.status_code}')