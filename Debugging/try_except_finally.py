while True: 
	try: 
		num = int(input('Por favor entre com um número: '))
	except ValueError: 
		print('Isso não é um número')
	else: # Else só irá rodar quando except não rodar
		print('Bom trabalho, você entrou um número')
		break
	finally: # Finally sempre irá rodar
		print('Sempre irá rodar')


