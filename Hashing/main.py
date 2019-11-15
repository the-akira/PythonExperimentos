import bcrypt

password = b'SecretPassword55'
pwd = b'SecretPass'

hashed = bcrypt.hashpw(password, bcrypt.gensalt(rounds=12)) 

if bcrypt.checkpw(password, hashed):
	print('It matches!')
else:
	print('Did not match')