import random

class color:
    DERROTA = '\033[91m'
    VITORIA = '\033[92m'
    EMPATE = '\033[94m'

opcoes = ['pedra', 'papel', 'tesoura']
maquina = random.choice(opcoes)
jogando = True 

while jogando == True:
	print('\n')
	print("# pedra")
	print("# papel")
	print("# tesoura")
	print("# sair")
	print('\n')
	player = input('Escolha entre uma das opções:\n\n')
	if maquina == player.lower():
		print(f'{color.EMPATE}Ocorreu um empate')
	elif player.lower() == 'pedra':
		if maquina == 'papel':
			print(f'{color.DERROTA}Você perdeu! {maquina} cobre {player.lower()}')
		else:
			print(f'{color.VITORIA}Parabéns! Você venceu! {player.lower()} quebra {maquina}')
	elif player.lower() == 'papel':
		if maquina == 'tesoura':
			print(f'{color.DERROTA}Você perdeu! {maquina} corta {player.lower()}')
		else:
			print(f'{color.VITORIA}Parabéns! Você venceu! {player.lower()} cobre {maquina}')
	elif player.lower() == 'tesoura':
		if maquina == 'pedra':
			print(f'{color.DERROTA}Você perdeu! {maquina} esmaga {player.lower()}')
		else:
			print(f'{color.VITORIA}Parabéns! Você venceu! {player.lower()} corta {maquina}')
	elif player.lower() == 'sair':
		jogando = False
	else:
		print('Jogada inválida, verifique se digitou a opção corretamente!')
	maquina = random.choice(opcoes)