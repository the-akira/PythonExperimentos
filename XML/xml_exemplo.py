import os 
import xml.etree.ElementTree as et 

# Caminho do diretório root
base_path = os.path.dirname(os.path.realpath(__file__))
print(base_path)

# Caminho do arquivo
xml_file = os.path.join(base_path, 'product_listing.xml')
print(xml_file)

tree = et.parse(xml_file)
print(type(tree))

root = tree.getroot()

for child in root:
	print(child.tag, child.attrib)

for child in root:
	for element in child:
		print(f'{element.tag} : {element.text}')
	print(' ')

new_product = et.SubElement(root, 'product', attrib={'id':'4'})
new_prod_name = et.SubElement(new_product, 'name')
new_prod_desc = et.SubElement(new_product, 'description')
new_prod_cost = et.SubElement(new_product, 'cost')
new_prod_ship = et.SubElement(new_product, 'shipping')

new_prod_name.text = 'Calca Python'
new_prod_desc.text = 'Muito legais'
new_prod_cost.text = '39.11'
new_prod_ship.text = '3.00'

tree.write('new_product_listing.xml')