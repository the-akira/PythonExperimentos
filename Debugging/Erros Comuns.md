# Alguns dos Erros Comuns encontrados em Python

## SyntaxError

- Erro que ocorre quando Python encontra alguma sintáxe incorreta (algo que ele não consegue fazer o parse)
- Usualmente ocorre por erros de digitação ou pela falta de conhecimento da linguagem
- Exemplo:

```python
def first:

None = 1

return 
```

## NameError

- Ocorre quando a variável não está definida, em outras palavras, nenhum valor foi atribuído a ela
- Exemplo:

```python
teste
```
## TypeError

- Ocorre quando é aplicado a uma operação ou função a um tipo errado
- Python não pode interpretar uma operação em dois tipos de dados
- Exemplo: 

```python
len(5)

'legal' + []
```

## IndexError

- Ocorre quando você tenta acessar um elemento em uma lista utilizando um índice inválido
- Exemplo:

```python
lista = ['teste']
lista[2]
```

## ValueError

- Ocorre quando uma operação construída ou função recebe um argumento que possui o tipo correto, porém um valor inapropriado

```python
int('teste')
```

## KeyError

- Ocorre quando um dicionário não tem a chave específica que estamos tentando acessar

```python
d = {}
d['chave']
```

## AttributeError

- Ocorre quando uma variável não tem um atributo

```python
'string teste'.atributo
```
