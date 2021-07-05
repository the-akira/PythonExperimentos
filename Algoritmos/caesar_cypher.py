alpha = 'abcdefghijklmnopqrstuvwxyz'

def encrypt(message, key):
    cyphertext = ""
    for char in message:
        if char in alpha:
            newpos = (alpha.find(char) + key) % 26
            cyphertext += alpha[newpos]
        else:
            cyphertext += char
    return cyphertext

message = input('Digite a mensagem a ser codificada: ')
message = message.lower()
chave = int(input('Informe o número da chave criptográfica: '))
encrypted = encrypt(message, chave)
print(f'Mensagem codificada: {encrypted}')

def decrypt(message, key):
    result = ""
    for letter in message:
        if letter in alpha:
            index = (alpha.find(letter) - key) % len(alpha)
            result = result + alpha[index]
        else:
            result = result + letter
    return result

def decrypt_brute_force(message):
    for key in range(len(alpha)):
        translated = ''
        for symbol in message:
            if symbol in alpha:
                num = alpha.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(alpha)
                translated = translated + alpha[num]
            else:
                translated = translated + symbol
        print(f'Hackeando a chave {key} = {translated}')

decrypted = decrypt(encrypted, chave)
print(f'Mensagem decodificada: {decrypted}\n')
decrypt_brute_force(encrypted)