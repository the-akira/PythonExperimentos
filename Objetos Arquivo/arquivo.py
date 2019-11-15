# MÈTODO 1

# with open('teste.txt') as f:

# 	for line in f:
# 		print(line, end='')

# MÈTODO 2

# with open('teste.txt') as f:

# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# 	f_contents = f.read(100)
# 	print(f_contents, end='')

# MÈTODO 3

# with open('teste.txt') as f:

# 	tamanho = 10

# 	f_contents = f.read(tamanho)

# 	print(f.tell())

	# while len(f_contents) > 0:
	# 	print(f_contents, end='*')
	# 	f_contents = f.read(tamanho)

# MÉTODO 4

# with open('teste2.txt', 'w') as f:
# 	f.write('test')
# 	f.seek(0)
# 	f.write('Ra')

with open('teste.txt', 'r') as rf:
	with open('teste_copia.txt', 'w') as wf:
		for line in rf: 
			wf.write('---\n' + line)

# MÉTODO 5

with open('art.jpg', 'rb') as rf:
	with open('art_copia.jpg', 'wb') as wf:
		chunk_size = 4096
		rf_chunk = rf.read(chunk_size)
		while len(rf_chunk) > 0:
			wf.write(rf_chunk)
			rf_chunk = rf.read(chunk_size)