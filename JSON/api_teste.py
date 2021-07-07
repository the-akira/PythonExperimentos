import json 
import requests 

r = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = r.json()

for post in posts:
    print(post) # Imprime todos os posts
    print(post['id']) # Imprime todos os ids
    print(post['title']) # Imprime todos os títulos
    print(post['body']) # Imprime todos os textos