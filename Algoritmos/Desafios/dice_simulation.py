"""
Escrever uma função Python para
determinar a probabilidade de certos
resultados quando rolando dados

Input:
Um variável número de argumentos
para os lados dos dados

Output:
Tabela de probabilidade para cada
resultado possível
"""

from collections import Counter
from random import randint

def roll_dice(*dice, num_trials=1_000_000):
    counts = Counter()
    for roll in range(num_trials):
        counts[sum((randint(1,sides) for sides in dice))] += 1

    print('Probabilidades')
    for outcome in range(len(dice), sum(dice) + 1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome]*100/num_trials))

roll_dice(4,6,6)