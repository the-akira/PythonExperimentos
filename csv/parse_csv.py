import csv

html_output = ''
names = []

# Opção com o método reader()

# with open('padrinhos.csv', 'r') as data_file:
# 	csv_data = csv.reader(data_file)

# 	# Pulando as duas primeiras linhas
# 	next(csv_data)
# 	next(csv_data)

# 	for line in csv_data:
# 		if line[0] == 'No Reward':
# 			break
# 		names.append(f'{line[0]} {line[1]}')

# for name in names:
# 	print(name)

# Outra opção é ler com DictReader()

with open('padrinhos.csv', 'r') as data:
	csv_data = csv.DictReader(data)

	next(csv_data)

	for line in csv_data:
		if line['FirstName'] == 'No Reward':
			break
		names.append(f"{line['FirstName']} {line['LastName']}")

# 	for item in csv_data:
# 		print(item)

html_output += f'<p> Existem atualmente {len(names)} contribuidores.</p>'	
html_output += '\n<ul>'
for name in names:
	html_output += f'\n\t<li>{name}</li>'
html_output += '\n</ul>'

print(html_output)




