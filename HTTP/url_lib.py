from urllib import request

resp = request.urlopen('https://wikipedia.org')
print(type(resp))
print(dir(resp))
print(resp.code)
print(resp.length)
print(resp.peek())

dados = resp.read()
print(type(dados))
print(len(dados))

html = dados.decode('UTF-8')
print(type(html))