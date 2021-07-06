from string import Template

# Nossa classe altera o delimitador do Template de $ para #
class MeuTemplate(Template):
    delimiter = '#'

livros = []
livros.append(dict(nome="Brave New World", autor='Aldous Huxley', id=2))
livros.append(dict(nome="1984", autor='George Orwell', id=5))	
livros.append(dict(nome="The Lord of The Rings", autor='J.R.R Tolkien', id=7))

t = MeuTemplate("Título do Livro: #nome, Autor: #autor, ID: #id")
print("Livros:")
for livro in livros:
    print(t.substitute(livro))