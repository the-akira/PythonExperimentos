"""
Projetar uma stack que suporte:
- push(x) -> None; adiciona x à stack
- top() -> x; vê o elemento do topo da stack e retorna ele
- pop() -> x; remove o elemento do topo da stack e retorna ele
- getMin() -> x; retorna o menor valor da stack

Restrições:
- Todas as operações devem executar em tempo constante, O(1)
"""

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if self.min_stack:
            self.min_stack.append(
                min(x, self.min_stack[-1])
            )
        else:
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()     
        else:
            pass

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return -1

    def get_min(self):
        if self.min_stack:
            return self.min_stack[-1]
        else:
            return -1

stack = MinStack()
stack.push(1)
stack.push(3)
stack.push(8)
print(stack.pop())
print(stack.top())
print(stack.get_min())