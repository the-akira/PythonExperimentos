import json

def install_sort(package):
    return package['analytics']['30d']

with open('package_info.json', 'r') as f:
    data = json.load(f)

# Filtra pacotes com video na descrição
data = [item for item in data if 'video' in item['desc']] 
data.sort(key=install_sort, reverse=True)
data_string = json.dumps(data, indent=2)
print(data_string)