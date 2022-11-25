"""
Dado um caminho (path). O caminho canônico deve ter o seguinte formato:

- Começa com '/'.
- Quaisquer dois diretórios são separados por uma única barra '/'.
- Não termina com '/' à direita.
- Contém apenas os diretórios no caminho do diretório raiz para 
o arquivo ou diretório de destino (exemplo: sem ponto '.' ou ponto duplo '..')

Dado um caminho, retorne o caminho canônico.

Restrições:
- 1 <= path.length <= 3000
- path é um caminho UNIX válido
- caminho contém letras, dígitos, pontos, barras e underscores

Exemplos:

Input: /home/
Output: /home

Input: /../
Output: /

Input: /home//1337/./
Output: /home/1337

Input: /home/../../tmp//./
Output: /tmp
"""

def simplify_path(path):
    stack = []
    for directory in path.split("/"):
        if directory == "":
            pass
        elif directory == ".":
            pass
        elif directory == "..":
            if stack:
                stack.pop()
            else:
                pass
        else:
            stack.append(directory)
    return "/" + "/".join(stack)

print(simplify_path("/home/"))
print(simplify_path("/../"))
print(simplify_path("/home//1337/./"))
print(simplify_path("/home/../../tmp//./"))