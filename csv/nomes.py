import csv

# with open('novos_nomes.csv', 'r') as csv_file:
# 	csv_reader = csv.reader(csv_file, delimiter='\t')

# 	for line in csv_reader:
# 		print(line)

with open('nomes.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file) # Leitura como dicionário 

	with open('novos_nomes.csv', 'w') as new_file:
		fieldnames = ['first_name', 'last_name']
		csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter=',')
		csv_writer.writeheader()

		for line in csv_reader:
			del line['email']
			csv_writer.writerow(line)
