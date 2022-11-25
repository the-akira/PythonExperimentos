"""
Given N bulbs, either on (1) or off (0).

Turning on i-th bulb causes all remaining bulbs on the right to flip.

Find the min number of switches to turn all the bulbs on.

Constraints:
- 1 <= N <= 1e5
- A[i] = {0, 1}
"""

def bulbs(array):
    cost = 0
    for element in array:
        if cost % 2 == 0:
            element = element
        if element % 2 == 1:
            continue
        else:
            cost += 1
    return cost

print(bulbs([1,0,1,1,0,1,1]))