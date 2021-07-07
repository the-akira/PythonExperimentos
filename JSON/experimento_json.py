import json

pessoas_json = """
{
    "pessoas": [
	{
        "nome": "Rafael dos Santos",
        "telefone": "48-99874-5537",
        "emails": ["rafasantos@gmail.com", "santosrafa@google.com"],
        "licença": false
	},
	{
        "nome": "Maria Sofia",
        "telefone": "48-98874-1247",
        "emails": null,
        "licença": true
	}
  ]	
}
"""

# Converte para um dicionário Python
data = json.loads(pessoas_json) 
print(type(data['pessoas']))
print(type(data))
print(data)

for pessoas in data['pessoas']:
    del pessoas['telefone']

novo_json = json.dumps(data, indent=2, sort_keys=True, ensure_ascii=False)
print(novo_json)