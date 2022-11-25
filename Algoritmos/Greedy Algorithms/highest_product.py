"""
Given an array of N integers.

Find the highest product by multiplying 3 elements.

Constraints:
- 3 <= N <= 5e5

Considerations:
- Take the highest 3 elements
- Consider: lowest 2 and highest 1

Example:
Input: [1,2,3,4]
Output: 2 * 3 * 4 = 24

Input: [0,-1,10,7,5]
Output: 5 * 7 * 10 = 350
"""

def highest_product(array):
    array.sort()
    highest_three = array[-1] * array[-2] * array[-3]
    lowest_two = array[0] * array[1] * array[-1]
    return max(highest_three, lowest_two)

print(highest_product([-2,-5,3,0,1,2,3]))
print(highest_product([3, 1, -2, 1, 5]))