import bcrypt

password = b'SecretPassword55'
pwd = b'SecretPass'

hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12)) 

if bcrypt.checkpw(password, hashed):
    print('Correspondente!')
else:
    print('Não correspondente!')