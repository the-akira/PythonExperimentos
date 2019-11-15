import json
# -*- coding: utf-8 -*-

people_string = """
{
	"people": [
	{
		"name": "Jose Paulo",
		"phone": "48-99874-5537",
		"emails": ["josepaulo@gmail.com", "paulojose@trabalho.com"],
		"has_license": false
	},
	{
		"name": "Maria Joao",
		"phone": "48-98874-1247",
		"emails": null,
		"has_license": true
	}
  ]	
}
"""

data = json.loads(people_string) # Converte para um dicionário Python
# print(type(data['people']))
# print(type(data))
# print(data)

for person in data['people']:
	del person['phone']

new_string = json.dumps(data, indent=2, sort_keys=True)
print(new_string)