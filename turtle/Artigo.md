# Desenhando com o Módulo Python Turtle

## Introdução

**Turtle graphics** é uma forma popular de apresentar a programação às crianças. Era parte da linguagem de programação [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) desenvolvida por Wally Feurzeig, Seymour Papert e Cynthia Solomon em 1967.

Imagine uma tartaruga robótica começando em **(0, 0)** no plano x-y. Depois de importar turtle (`import turtle`), é possível dar comandos a ela, como por exemplo `turtle.forward(100)`, e ela se move (na tela!) 100 pixels na direção para a qual está voltada, desenhando uma linha conforme se move. Dar a ela o comando `turtle.right(90)`, faz ela girar 90 graus no local no sentido horário.

Ao combinar esses comandos e outros semelhantes, formas e imagens complexas podem ser facilmente desenhadas.

## A Biblioteca turtle

[turtle](https://docs.python.org/3/library/turtle.html) é uma biblioteca Python pré-instalada que permite aos usuários criar imagens e formas fornecendo-lhes uma tela de pintura virtual. A caneta na tela que usamos para desenhar é chamada de **turtle** e é isso que dá nome à biblioteca. Resumindo, a biblioteca Python turtle ajuda os novos programadores a ter uma ideia de como é a programação com Python de uma forma divertida e interativa.

Uma vez que a biblioteca turtle já é construída no Python, então não precisamos instalar nenhum pacote, apenas devemos ter o Python em nossa máquina e então importá-la em nosso ambiente. 

Neste exemplo vamos abrir o interpretador do Python digitando o seguinte comando em nosso terminal:

```python
python3
```

Se desejar, você pode optar pelo interpretador online [REPL](https://repl.it/new/python_turtle). 

Agora que temos acesso ao interpretador de comandos da linguagem Python, podemos finalmente importar o módulo turtle:

```python
import turtle
```

Uma vez que a biblioteca turtle está em nosso ambiente Python, podemos começar a programar com ela. turtle é uma biblioteca gráfica, o que significa que precisaremos criar uma janela separada (chamada de tela) para executar cada comando de desenho. Podemos criar essa tela inicializando uma variável para ela da seguinte maneira:

```python
s = turtle.getscreen()
```

Ao executarmos o comando acima, veremos que será aberta uma janela separada:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/screen.png)

Esta janela é chamada de tela. É onde podemos ver o *output* de nosso código. A pequena forma triangular preta no meio da tela é chamada de turtle.

Em seguida, devemos inicializar a variável **t**, que será usada em todo o programa para se referir à turtle:

```python
t = turtle.Turtle()
```

Finalmente temos a **tela** e a **turtle**. A tela atua como uma tela de pintura, enquanto a turtle atua como uma caneta. Podemos programar a turtle para se mover pela tela. A turtle tem certas características mutáveis, como **tamanho**, **cor** e **velocidade**. Ele sempre aponta para uma direção específica e se moverá nessa direção, a menos que digamos o contrário:

- Quando estiver para cima (**up**), significa que nenhuma linha será desenhada quando ela se mover.
- Quando está para baixo (**down**), significa que uma linha será desenhada quando ela se mover.

## Programando com turtle