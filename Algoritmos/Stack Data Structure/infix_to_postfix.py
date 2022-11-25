operators = set(['+', '-', '*', '/', '(', ')', '^'])
priority = {'+':1, '-':1, '*':2, '/':2, '^':3} 
 
def infix_to_postfix(infix): 
    stack = []
    output = '' 

    for character in infix:
        if character not in operators:
            output += character
        elif character=='(':
            stack.append('(')
        elif character==')':
            while stack and stack[-1]!= '(':
                output += stack.pop()
            stack.pop()
        else: 
            while stack and stack[-1] !='(' and priority[character] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(character)
    while stack:
        output += stack.pop()
    return output

print(infix_to_postfix("a+b/c*d-e"))