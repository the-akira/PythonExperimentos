# Alguns dos Erros Comuns encontrados em Python

## SyntaxError

- Erro que ocorre quando Python encontra alguma sintaxe incorreta (algo que ele não consegue fazer o **[parsing](https://en.wikipedia.org/wiki/Parsing)**).
- Usualmente ocorre por erros de digitação ou pela falta de conhecimento da linguagem.

#### Exemplo:

```python
def func:

None = 1

return 
```

## NameError

- Ocorre quando a variável não está definida, em outras palavras, nenhum valor foi atribuído a ela.

#### Exemplo:

```python
nome
```
## TypeError

- Ocorre quando uma operação ou função é aplicado a um tipo errado.
- Python pode não interpretar algumas operações em dois tipos de dados diferentes.

#### Exemplo: 

```python
len(5)

'string' + []

{} + 1.5
```

## IndexError

- Ocorre quando você tenta acessar um elemento em uma lista utilizando um índice inválido.

#### Exemplo:

```python
lista = [1, 2, 3, 4, 5]
lista[6]
```

## ValueError

- Ocorre quando uma operação construída ou função recebe um argumento que possui o tipo correto, porém um valor inapropriado.

#### Exemplo:

```python
int('string')
```

## KeyError

- Ocorre quando um dicionário não tem a chave específica que estamos tentando acessar.

#### Exemplo:

```python
d = {}
d['chave']
```

## AttributeError

- Ocorre quando uma variável não tem um atributo.

#### Exemplo:

```python
'string'.imag
```