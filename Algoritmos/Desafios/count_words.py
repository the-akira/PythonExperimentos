import collections
import re

"""
Escrever uma função Python que contará
o número de palavras únicas e suas ocorrências

Input:
Caminho para o arquivo de texto

Output:
Imprimir uma mensagem com:
- Número total de palavras
- Top 20 palavras mais frequentes
"""

def count_words(path):
    with open(path, encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'Total words: {len(all_words)}')

        word_counts = collections.Counter(all_words)

        print('\nTop 20 Words:')
        for word in word_counts.most_common(20):
            print(word[0], '\t', word[1])

count_words('input.txt')