import operator

def eval_reverse_polish_notation(tokens):
    stack = []

    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    for token in tokens:
        if token not in ops:
            stack.append(int(token))
        else:
            n2 = stack.pop()
            n1 = stack.pop()
            result = ops[token](n1,n2)
            stack.append(int(result))
    return stack[0]

print(eval_reverse_polish_notation("01-33*7/+"))