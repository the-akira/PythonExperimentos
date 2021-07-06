import csv

with open('nomes.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file) 

    with open('nomes_alterados.csv', 'w') as new_file:
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)

with open('nomes_alterados.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')

    for line in csv_reader:
        print(line)