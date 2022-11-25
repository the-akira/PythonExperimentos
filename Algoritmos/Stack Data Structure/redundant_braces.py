"""
Uma string A contém operadores, parênteses e letras.

Retorne 1 se A tiver parênteses redundantes, caso contrário, retorne 0.

Restrições:
- 1 <= N ,+ 1e5

Exemplos:

Input: ((a+b))
Output: 1

Input: (a+(a+b))
Output: 0
"""

def redundant_braces(A):
    stack = []
    for character in A:
        if character != ")":
            stack.append(character)
        else:
            count = 0
            while stack[-1] != "(":
                popped = stack.pop()
                if popped in "+-*/":
                    count += 1
            stack.pop()

            if count == 0:
                return 1
    return 0

print(redundant_braces("((a+b))"))
print(redundant_braces("(a+(a+b))"))