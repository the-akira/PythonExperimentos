# Desenhando com o Módulo Python Turtle

## Introdução

**Turtle graphics** é uma forma popular de apresentar a programação às crianças. Era parte da linguagem de programação [Logo](https://en.wikipedia.org/wiki/Logo_(programming_language)) desenvolvida por Wally Feurzeig, Seymour Papert e Cynthia Solomon em 1967.

Imagine uma tartaruga robótica começando em **(0, 0)** no plano x-y. Depois de importar turtle (`import turtle`), é possível dar comandos a ela, como por exemplo `turtle.forward(100)`, e ela se move (na tela!) 100 pixels na direção para a qual está voltada, desenhando uma linha conforme se move. Dar a ela o comando `turtle.right(90)`, faz ela girar 90 graus no local no sentido horário.

Ao combinar esses comandos e outros semelhantes, formas e imagens complexas podem ser facilmente desenhadas.

## A Biblioteca Turtle

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

Esta janela é chamada de tela. É onde podemos ver o *output* de nosso código. A pequena forma triangular preta no meio da tela é chamada de turtle. É possível escondermos ela com o comando **hideturtle()**:

```python
turtle.hideturtle()
```

Observe que ao executarmos este comando, ele fará com que a turtle desapareça, para fazermos com que ela apareça novamente, podemos usar o comando **Turtle()**.

Em seguida, vamos inicializar uma variável **t**, que será usada em todo o programa para se referir à turtle:

```python
t = turtle.Turtle()
```

Finalmente temos a **tela** e a **turtle**, que neste caso será referenciada pela variável **t**. A tela atua como uma tela de pintura, enquanto a turtle atua como uma caneta. Podemos programar a turtle para se mover pela tela. A turtle tem certas características mutáveis, como **tamanho**, **cor** e **velocidade**. Ele sempre aponta para uma direção específica e se moverá nessa direção, a menos que digamos o contrário:

- Quando estiver para cima (**up**), significa que nenhuma linha será desenhada quando ela se mover.
- Quando está para baixo (**down**), significa que uma linha será desenhada quando ela se mover.

## Programando com Turtle

Como já vimos, a turtle inicia na posição (0,0) no plano x-y e podemos obter sua posição atual através do comando position:

```python
t.position() # (0.00,0.00)
```

### Movendo a Turtle

É possível mover a turtle em quatro direções diferentes:

- Forward (Para frente)
- Backward (Para trás)
- Left (Esquerda ou Anti-Horário)
- Right (Direita ou Horário)

Para compreendermos melhor estas ideias, vamos experimentar alguns comandos. 

Começamos alterando a direção da turtle em **90 graus** para a **esquerda**:

```python
t.left(90)
```

Estamos agora apontando para o norte, vamos então nos mover **100 unidades** para frente:

```python
t.forward(100)
```

Novamente, vamos alterar a direção da turtle em **180 graus** para a **direita**:

```python
t.right(180)
```

Estamos agora apontando para o sul, vamos então nos mover **100 unidades** para trás:

```python
t.backward(100)
```

Eventualmente obteremos o seguinte resultado:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/commands.png)

É possível também usar atalhos para estes comandos:

- **t.rt()** para `t.right()`
- **t.fd()** para `t.forward()`
- **t.lt()** para `t.left()`
- **t.bk()** para `t.backward()`

Podemos também traçar uma linha de nossa posição atual para qualquer outra posição arbitrária na tela. Isso é feito com o auxílio das coordenadas:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/PythonTurtle.png)

A tela é dividida em quatro quadrantes. O ponto onde a tartaruga é inicialmente posicionada no início do programa é (0,0). Este ponto é chamado de **Home**. 

Para mover a tartaruga para qualquer outra área da tela, podemos usar o comando **goto()** e inserir as coordenadas desta forma:

```python
t.goto(-100,100)
```

Nossa turtle irá se mover diretamente ao ponto (-100,100), desenhando uma linha:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/goto.png)

Para fazermos a turtle retornar à posição **home**, podemos usar o seguinte comando:

```python
t.home()
```

Perceba que **home()** é apenas um atalho, o comando `t.goto(0,0)` teria o mesmo efeito.

### Desenhando Formas Geométricas

Podemos começar desenhando polígonos, que consistem em linhas retas conectadas em determinados ângulos.

Com a ajuda de um **[for loop](https://github.com/the-akira/Python-Iluminado/blob/master/Capitulos/14.ForLoops.md)**, podemos facilmente desenhar um octógono:

```python
for _ in range(8):
    t.rt(45)
    t.fd(65)
```

O *output* do código será o seguinte:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/octagon.png)

Podemos seguir uma lógica similar para desenhar um triângulo:

```python
for _ in range(3):
    t.fd(150)
    t.left(120)
```

Que nos trará o seguinte resultado:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/triangle.png)

A biblioteca turtle nos oferece um comando chamado de **circle()** que nos permite desenhar círculos:

```python
t.circle(80)
```

O número entre parênteses é o raio do círculo. Você pode aumentar ou diminuir o tamanho do círculo, alterando o valor de seu raio. Como *output* veremos um círculo:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/circle.png)

Da mesma forma, podemos também desenhar um ponto, que nada mais é do que um círculo preenchido. Para esta tarefa devemos usar o comando **dot()**:

```python
t.dot(50)
```

Que nos apresentará:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/dot.png)

### Comandos Úteis

#### Alterando a Cor da Tela

Por padrão, turtle sempre abre uma tela com um fundo branco. Entretanto, podemos alterar a cor da tela a qualquer momento usando o seguinte comando:

```python
turtle.bgcolor('gray')
```

Imediamente podemos observar que a cor de nossa tela irá alterar para cinza:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/color.png)

Neste caso estamos usando a cor *gray* (cinza), também podemos usar cores como *green* (verde) e *red* (vermelho). Neste site você pode ver uma lista com diversos nomes de cores: [Trinket.io](https://trinket.io/docs/colors)

Além disso, é possível informarmos o [valor hexadecimal](https://en.wikipedia.org/wiki/Web_colors) de uma cor. Portanto, se quisermos retornar para o branco, podemos digitar um dos seguintes comandos:

```python
turtle.bgcolor('#ffffff')
turtle.bgcolor('white')
```

Ambos são válidos e produzem o mesmo efeito.

#### Alterando o Título da Tela

É possível também alterarmos o título da nossa tela com o comando **title()**. Por exemplo:

```python
turtle.title("Aprendendo Python com a biblioteca Turtle!")
```

Veja que o texto de nossa barra de título será alterado:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/title.png)

Dessa maneira, podemos alterar o cabeçalho da tela de acordo com a nossa preferência.

#### Alterando o Tamanho da Turtle

Podemos aumentar ou diminuir o tamanho da turtle na tela para torná-la maior ou menor. Isso altera apenas o tamanho da forma da turtle, sem afetar o *output* da caneta conforme ela desenha na tela, por exemplo:

```python
t.shapesize(5,5,10)
```

Aqui estamos passando os seguintes parâmetros para alterar o tamanho da turtle:

- Comprimento
- Largura 
- Largura do contorno

Neste caso teremos o seguinte *output*:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/turtlesize.png)

#### Alterando o Tamanho da Caneta

O comando anterior foi responsável por mudar apenas o tamanho da forma da turtle. No entanto, às vezes, pode ser necessário aumentar ou diminuir a espessura da caneta, para esta tarefa podemos usar o seguinte comando:

```python
t.pensize(8)
t.goto(150,150)
```

Imediamente podemos ver o resultado:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/pensize.png)

Observe que aumentou a espessura da linha traçada pela turtle.

#### Alterando a Forma da Turtle

A forma inicial da turtle não é realmente uma tartaruga, mas uma figura triangular. Entretanto, é possível alterarmos a aparência da turtle e para isso nos é fornecido algumas opções, por exemplo:

```python
t.shape("turtle")
t.shape("arrow")
t.shape("circle")
t.shape("triangle")
t.shape('classic')
t.shape('square')
```

A forma da turtle irá alterar de acordo com a sua escolha, neste caso eu optei pela **turtle**:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/turtle.png)

#### Alterando Cores

Ao abrirmos uma nova tela pela primeira vez, a turtle começa como uma figura preta e desenha com tinta preta. Com base em seus requisitos, podemos fazer duas coisas:

- **Alterar a cor da turtle**: Isso altera a cor de preenchimento.
- **Alterar a cor da caneta**: Isso altera o contorno ou a cor da tinta.

Também é possível (se desejarmos) alterar ambos.

Para alterarmos a cor da tartaruga (ou o preenchimento), devemos digitar o seguinte comando:

```python
t.fillcolor("green")
```

Para alterarmos a cor da caneta (ou contorno), digitamos o seguinte:

```python
t.pencolor("#4da364")
```

Também é possível alterarmos ambos de uma só vez:

```python
t.color("#4da364","green")
```

No exemplo acima, a primeira cor é para a caneta e a segunda é para o preenchimento. Observe que alterar a cor da caneta e do preenchimento também altera a cor da tartaruga na tela de acordo, nos trazendo o seguinte resultado:

![img](https://raw.githubusercontent.com/the-akira/PythonExperimentos/master/turtle/Imagens/turtlecolor.png)