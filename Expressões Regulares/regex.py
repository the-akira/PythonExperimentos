import re

frase = "Eu acredito que entendi as expressões regulares"

match_result = re.match('eu', frase, re.M|re.I)
if match_result:
    print(f"Correspondência encontrada: {match_result.group()}")
else:
    print("Nenhuma correspondência encontrada!")

search_result = re.search('acredito', frase, re.M|re.I)
if search_result:
    print(f"Busca encontrada: {search_result.group()}")
else:
    print("Nada encontrado na busca!")