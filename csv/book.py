import csv 

with open('book.csv', newline='') as csv_file:
    csv_reader = csv.reader(csv_file)
    for linha in csv_reader:
        print(f"{linha[0]},{linha[1]}")