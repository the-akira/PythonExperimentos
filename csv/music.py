import csv 

with open('music.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    count = 0
    for linha in csv_reader:
        if linha[2] == 'Classical':
            count += 1
    print(f'Existem {count} pessoas que ouvem música clássica')