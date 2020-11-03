# O PRIMEIRO DO RANKING

Joãozinho está jogando fliperama e quer ser o primeiro no topo dos melhores e acompanhar o seu progresso. O jogo usa o modelo de classificação densa,
onde o jogador com a maior pontuação recebe a posição 1, e assim por diante. Jogadores que tiverem a mesma pontuação, recebem a mesma posição.
Por exemplo, para os 4 melhores jogadores com pontuações 100, 90, 90 e 80, as posições na classificação serão 1, 2, 2 e 3 respectivamente.
Se o joãozinho pontua 70, 80 e 105, sua classificaçao a cada rodada será 4º, 3º e 1º, respectivamente.
Descrição da Função
Complete a função o_primeiro_do_ranking abaixo. Ela deve retornar uma lista de inteiros onde cada elemento res[j] representa uma posição da classificação depois da rodada j.
A função possui os seguintes parametros:
* qtd_pontuacoes: um inteiro com a quantidade de pontuações da classificação.
* pontuacoes: uma lista de inteiros que representa as pontuacoes da classificação.
* qtd_pontuacoes_joaozinho =  um inteiro com a quantidade de pontuações do joãozinho.
* pontuacoes_do_joaozinho: Uma lista de inteiros que representa as pontuações do joãozinho a cada rodada.
A ideia da função é nos dizer a cada rodada (para cada item no parametro pontuacoes_do_joaozinho), a posição do joãozinho na classificação.
Restrições
1 <= n <= 2 x 10^5
1 <= m <= 2 x 10^5
0 <= pontuacoes[i] <= 10^9 para 0 <= i < n
0 <= pontuacoes_do_joaozinho[i] <= 10^9 para 0 <= j < m
A classificação atual, pontuacoes, está em ordem decrescente.
As pontuações do joãozinho, estão em ordem crescente.
Formato de saída
retorne uma lista de inteiros. O inteiro deve indicar a posição de Joãozinho depois de ter jogado a rodada respectiva. Exemplo
para a lista [5, 2, 1]:
    - na rodada 0, a posição do joãozinho era 5.
    - na rodada 2, a posição do joãozinho era 2.
    - na rodada 1, a posição do joãozinho era 1.
Exemplo de entrada 1
qtd_pontuacoes = 7
pontuacoes = [100, 100, 50, 40, 40, 20, 10]
qtd_pontuacoes_do_joaozinho = 4
pontuacoes_do_joaozinho = [5, 25, 50, 120]
_______________________________
|100 |100 | 50| 40| 40| 20| 10|
-------------------------------
Lista: pontuacoes
_________________
|5 |25 | 50| 120|
-----------------
Lista: pontuacoes_do_joaozinho
Exemplo de saída 1
[6, 4, 2, 1]
Explicação 1
Joãozinho começa jogando com 7 jogadores na classificação, como na tabela abaixo:
_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Shirley     | 20   |
| 5      | Carolaine   | 10   |
-------------------------------
Depois que o joãozinho terminou a rodada 0, sua pontuação é 5 e seu lugar na classificação é 6.
_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Shirley     | 20   |
| 5      | Carolaine   | 10   |
| 6      | Joãozinho   | 5    |
-------------------------------
Depois que o joãozinho terminei a rodada 1, sua pontuação é 25 e sua classificação é 4.
_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Joãozinho   | 25   |
| 5      | Shirley     | 20   |
| 6      | Carolaine   | 10   |
Depois que o joãozinho terminou a rodada 2, sua pontuação é 50 e sua classificação é em 2, empatado com o Adagalmir.
_______________________________
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Geraldo     | 100  |
| 1      | Geilson     | 100  |
| 2      | Adagalmir   | 50   |
| 2      | Joãozinho   | 50   |
| 3      | Valmira     | 40   |
| 3      | Cleberson   | 40   |
| 4      | Shirley     | 20   |
| 5      | Carolaine   | 10   |
Depois que o joãozinho terminou a rodada 3, sua pontuação é 120 e sua classificação é em 1.
| Posição |    Nome    | Nota |
-------------------------------
| 1      | Joãozinho   | 120  |
| 2      | Geraldo     | 100  |
| 2      | Geilson     | 100  |
| 3      | Adagalmir   | 50   |
| 4      | Valmira     | 40   |
| 4      | Cleberson   | 40   |
| 5      | Shirley     | 20   |
| 6      | Carolaine   | 10   |
Exemplo de entrada 2
qtd_pontuacoes = 6
pontuacoes = [100, 90, 90, 80, 75, 60]
qtd_pontuacoes_do_joaozinho = 5
pontuacoes_do_joaozinho = [50, 65, 77, 90, 102]
__________________________
|100 |90 | 90| 80| 75| 60|
--------------------------
Lista: pontuacoes
______________________
|50 |65 | 77| 90| 102|
----------------------
Lista: pontuacoes_do_joaozinho
Exemplo de saída 2
[6, 5, 4, 2, 1]