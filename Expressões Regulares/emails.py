import re

emails = '''
gabriel@gmail.com
gabriel.felippe@university.edu
gab-333-felippe@google.net
gabrielfelippe90@gmail.com
gabrielheavy@hotmail.com
'''

pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

matches = pattern.finditer(emails)
for match in matches:
    print(match)