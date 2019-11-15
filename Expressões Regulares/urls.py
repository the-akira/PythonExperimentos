import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#                                 G1     G2    G3
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') # G0 = TUDO

subbed_urls = pattern.sub(r'\2\3', urls) # GRUPO 2 e GRUPO 3

print(subbed_urls)

matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.group(3))