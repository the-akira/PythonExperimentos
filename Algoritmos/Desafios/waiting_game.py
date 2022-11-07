import random
import time

"""
O jogador receberá um tempo aleatório,
Quando o jogador pressiona a tecla Enter
Inicia-se um timer, o objetivo do jogador
é esperar o tempo especificado e depois
pressionar Enter novamente, será apresentado
ao jogador o tempo passado e se ele foi
certeiro, muito rápido ou muito lento.
"""

def waiting_game():
    target = random.randint(2,4)
    print(f'Seu tempo é {target} segundos')
    input('Pressione Enter para Iniciar')
    start = time.perf_counter()
    input(f'Pressione Enter novamenter após {target} segundos')
    elapsed = time.perf_counter() - start
    print(f'Tempo passado {elapsed:.3f}')
    if elapsed  == target:
        print('Perfeito')
    elif elapsed < target:
        print(f'{target-elapsed:.3f} segundos muito rápido')
    else:
        print(f'{elapsed-target:.3f} segundos muito devagar')       

waiting_game()