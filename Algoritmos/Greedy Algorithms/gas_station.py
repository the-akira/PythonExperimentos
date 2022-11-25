"""
There are N gas stations along a circular route.

Each has A[i] amount of gas.
To travel from station i -> i+1, there is B[i] cost.

Find the earliest station from where you can travel around the entire circuit.

Return -1 if not possible

Constraints:
- 1 <= N <= 1e6
"""

def can_complete_circuit(A, B):
    n = len(A)

    curr = start = 0
    for i, (gas, cost) in enumerate(zip(A*2, B*2)):
        if i == start + n:
            return start

        curr += gas - cost

        if curr < 0:
            start = i + 1
            curr = 0

    return -1

print(can_complete_circuit([3,5,2,1,7],[4,2,1,9,1]))