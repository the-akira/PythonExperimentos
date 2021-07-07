from urllib import request

# Requisição HTTP com urllib
resposta = request.urlopen('https://cc33z.netlify.app')
# Código de resposta HTTP
print(resposta.code)
# Peek
print(resposta.peek())

# Obtém os dados
dados = resposta.read()
print(dados)

# Decodifica em UTF-8
html = dados.decode('UTF-8')
print(html)