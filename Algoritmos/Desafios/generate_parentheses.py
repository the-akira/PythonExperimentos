"""
Given an integer n, generate all the valid 
combinations of n pairs of parentheses.

Exemplo:

Input: n = 3

Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

A combination that contains 1 type of parentheses is valid if 
every opening parentheses has its closing parentheses, and it
doesn't have a closing parentheses without having and unused
opening parenthesis before it.

Valid: ()((()))(())
Invalid: ()(()(())
Invalid: ()(()))(())
"""

# 1st solution
def is_valid(combination):
    stack = []
    for par in combination:
        if par == '(':
            stack.append(par)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

# 2nd solution
def is_valid_parentheses(combination):
    diff = 0
    for par in combination:
        if par == '(':
            diff += 1
        else:
            if diff == 0:
                return False
            else:
                diff -= 1
    return diff == 0

print(is_valid("()((()))(())"))
print(is_valid_parentheses("()(()(())"))

# Backtracking solution
def generate(n):
    def recursive(n, diff, combination, combinations):
        if diff < 0:
            return
        elif n == 0:
            if diff == 0:
                combinations.append(''.join(combination))
        else:
            combination.append('(')
            recursive(n - 1, diff + 1, combination, combinations)
            combination.pop()
            combination.append(')')
            recursive(n - 1, diff - 1, combination, combinations)
            combination.pop()
    combinations = []
    recursive(2 * n, 0, [], combinations)
    return combinations

parentheses = generate(3)
print(parentheses)