"""
Dada uma string de apenas "(" e ")".

Encontre a mais longa substring de parênteses válidos.

Restrições:
- 1 <= N <= 3e4

Exemplos:

Input: ()(((
Output: 2

Input: ()(((()
Output: 2
"""

def longest_valid_parentheses(s):
    n = len(s)
    is_ok = [0] * n
    stack = []

    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        else:
            if stack:
                is_ok[stack.pop()] = 1
                is_ok[i] = 1
            else:
                pass

    count = 0
    answer = 0
    for i in range(n):
        if is_ok[i]:
            count += 1
        else:
            count = 0
        answer = max(answer, count)
    return answer

print(longest_valid_parentheses("()((("))
print(longest_valid_parentheses("()(((()"))