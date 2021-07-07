import os 
import xml.etree.ElementTree as et 

# Caminho do diretório raiz
base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)

# Caminho do arquivo XML
xml_file = os.path.join(base_path, 'produtos.xml')
print(xml_file)

# Parsing do arquivo XML
tree = et.parse(xml_file)
print(type(tree))

# Obtém a raiz do arquivo XML
root = tree.getroot()

# Imprime as tags
for child in root:
    print(child.tag, child.attrib)

# Imprime os elementos
for child in root:
    for element in child:
        print(f'{element.tag} : {element.text}')
    print(' ')

# Criando um novo produto
new_product = et.SubElement(root, 'product', attrib={'id':'4'})
new_prod_name = et.SubElement(new_product, 'name')
new_prod_desc = et.SubElement(new_product, 'description')
new_prod_cost = et.SubElement(new_product, 'cost')
new_prod_ship = et.SubElement(new_product, 'shipping')

new_prod_name.text = 'Livro Python'
new_prod_desc.text = 'Aprenda a linguagem Python'
new_prod_cost.text = '39.50'
new_prod_ship.text = '3.00'

# Escrever novos dados em um novo arquivo
tree.write('novos_produtos.xml')