import csv 

with open('book.csv', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('book_alterado.csv', 'w') as novo_arquivo:
        fieldnames = ['Title', 'Author', 'Genre']
        csv_writer = csv.DictWriter(novo_arquivo, fieldnames=fieldnames, delimiter=';')
        csv_writer.writeheader()

        for linha in csv_reader:
            del linha['Height']
            del linha['Publisher']
            csv_writer.writerow(linha)