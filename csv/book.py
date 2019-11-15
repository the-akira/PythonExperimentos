import csv 

with open('book.csv', newline='') as csv_file:
	csv_reader = csv.reader(csv_file)
	print(type(csv_reader))
	for linha in csv_reader:
		print(f"{linha[0]},{linha[1]}")