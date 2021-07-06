import re

urls = '''
https://www.google.com
http://akiradev.netlify.app
https://youtube.com
https://www.nasa.gov
'''

#                                 G1     G2    G3
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # G0 = TUDO

substituir_urls = pattern.sub(r'\2\3', urls) # GRUPO 2 e GRUPO 3
print(substituir_urls)

matches = pattern.finditer(urls)
for match in matches:
    print(f'G0 = {match.group(0)}')
    print(f'G1 = {match.group(1)}')
    print(f'G2 = {match.group(2)}')
    print(f'G3 = {match.group(3)}')