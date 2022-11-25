"""
Dada uma string 's' apenas de parênteses.

Retorne True se 's' é válida, caso contrário, retorne False.

Restrições:
- 1 <= N <= 1e5

Exemplos:

Input: ({}[])
Output: True

Input: ({)
Output: False
"""

def is_valid(s):
    stack = []
    mapping = {
        "}": "{",
        ")": "(",
        "]": "[",
    }
    for character in s:
        if character in "([{":
            stack.append(character)
        else:
            if stack:
                if mapping[character] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                return False
    return len(stack) == 0

print(is_valid("({}[])"))
print(is_valid("({)"))
print(is_valid("()"))