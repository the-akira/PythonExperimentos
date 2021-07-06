import csv

html_output = ''
names = []

with open('colaboradores.csv', 'r') as data:
    csv_data = csv.DictReader(data)

    next(csv_data)

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p> Existem atualmente {len(names)} contribuidores.</p>'	
html_output += '\n<ul>'
for name in names:
	html_output += f'\n\t<li>{name}</li>'
html_output += '\n</ul>'
print(html_output)