while True: 
    try: 
        num = int(input('Por favor informe um número: '))
    except ValueError: 
        print('Isso não é um número')
    else: # Else só irá executar quando except não executar
        print('Bom trabalho, você entrou um número')
        print(f'Número escolhido = {num}')
        break
    finally: # Finally sempre irá executar
        print('Sempre irá executar!')