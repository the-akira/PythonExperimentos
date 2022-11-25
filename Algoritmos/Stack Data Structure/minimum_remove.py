"""
Uma string 's' contém "(",.")" e letras em inglês lowercase.

Remova o mínimo número de parênteses para fazer 's' ser válido.

Restrições:
- 1 <= len(s) <= 1e5

Exemplos:

Input: (tan(ishq)
Output: tan(ishq)

Input: (1337)
Output: (1337)
"""

def min_remove_to_make_valid(s):
    is_ok = [0] * len(s)
    stack = []

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                is_ok[stack.pop()] = 1
                is_ok[i] = 1
            else:
                continue
        else:
            continue
    answer = ""
    for i, c in enumerate(s):
        if c in "()":
            if is_ok[i]:
                answer += c
            else:
                pass
        else:
            answer += c
    return answer

print(min_remove_to_make_valid("(tan(ishq)"))
print(min_remove_to_make_valid("(1337)"))