# Blockchain

Uma [blockchain](https://en.wikipedia.org/wiki/Blockchain) é uma lista crescente de registros, chamados de blocos, que são vinculados por meio de criptografia. Cada bloco contém um **hash criptográfico do bloco anterior**, um **timestamp** e **dados de transação** (geralmente representados como uma **Merkle tree**). O **timestamp** prova que os dados da transação existiam quando o bloco foi publicado de forma a entrar em seu hash. Como cada bloco contém informações sobre o bloco anterior a ele, eles formam uma cadeia, com cada bloco adicional reforçando os anteriores. Portanto, as cadeias de blocos são resistentes à modificação de seus dados porque, uma vez registrados, os dados em qualquer bloco não podem ser alterados retroativamente sem alterar todos os blocos subsequentes.

## Usando a Blockchain

O programa Blockchain criado tem como objetivo simular um blockchain simples de *cryptocurreny*. O usuário executará uma web API em seu **localhost** que permite hospedar, criar seu próprio Blockchain e se comunicar com outros Blockchains.

Precisamos de uma maneira de fazer solicitações **POST** ou **GET** para a nossa API ou API de outro nó. Algo como **Postman** ou **cURL** são boas ferramentas para usar, neste exemplo usaremos **cURL**.

Também é necessário instalar as bibliotecas [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/) e [Requests](https://docs.python-requests.org/en/latest/user/install/#install):

```
pip install Flask
pip install requests
```

Com Flask e Requests instaladas, devemos executar o aplicativo com o seguinte comando:

```
python block_chain.py
```

### Fazendo Requisições

#### Minerando 

Minere um novo bloco a ser adicionado ao Blockchain deste nó, o minerador será recompensado com uma moeda.

``` 
curl --location --request GET 'http://localhost:5000/mine' --data-raw ''
```

#### Verificando

Verifique os Blockchains de outros nós registrados e chegue a um consenso de qual cadeia é mais confiável.

A cadeia de maior autoridade é a Blockchain mais longa com a maioria dos blocos.

A *authoritative chain* é copiada como o novo Blockchain.

```
curl --location --request GET 'http://localhost:5000/nodes/resolve' --data-raw ''
```

#### Registrando

Registre outro computador nó para este Blockchain.

O parâmetro "nodes" postado será o endereço IP do nó que você deseja adicionar. Neste exemplo, é `http://localhost:5000`.

```
curl -d '{"nodes":"http://localhost:5000"}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/nodes/register
```

#### Blockchain

Retorna o Blockchain atual deste computador nó:

```
curl --location --request GET 'http://localhost:5000/chain'
```

#### Transação

Crie uma nova transação que será armazenada no próximo Bloco criado.

```
curl -d '{"sender":"gabriel","recipient":"rafael","amount":50}' -H "Content-Type: application/json" -X POST http://0.0.0.0:5000/transactions/new
```

#### Sync

Copia a cadeia do nó postado.

```
curl --location --request POST 'http://localhost:5000/nodes/sync' --header 'Content-Type: application/json' --data-raw '{"nodes": "http://localhost:5000"}'
```