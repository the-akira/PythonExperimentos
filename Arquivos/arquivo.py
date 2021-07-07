with open('teste.txt', 'r') as rf:
    with open('teste_copia.txt', 'w') as wf:
        for line in rf: 
            wf.write('---\n' + line)

with open('art.jpg', 'rb') as rf:
    with open('art_copia.jpg', 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)