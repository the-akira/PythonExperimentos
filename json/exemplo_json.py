import json

personagem = {
  "nome": "Talantyr",
  "epiteto": "O Glorioso",
  "nível": 45,
  "vivo": True,
  "atributos": {"força": 45, "destreza": 60, "inteligência": 70},
  "mascotes": ("Lobo","Coruja"),
  "magias": None,
  "itens": [
    {"nome": "poção de mana", "quantidade": 5},
    {"nome": "poção de vida", "quantidade": 7}
  ]
}

print(json.dumps(personagem, ensure_ascii=False, indent=4, sort_keys=True))