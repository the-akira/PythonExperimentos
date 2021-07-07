import json

# Carrega o arquivo 'states.json'
with open('states.json') as f:
    data = json.load(f)

# Remove o atributo 'area_codes'
for state in data['states']:
    del state['area_codes']

# Salva as alterações em um novo arquivo 'new_states.json'
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)