"""
Given an array of integers of length N.

Majority element occurs with E > [N/2] frequency.

Find the majority element.

Constraints:
- 1 <= N <= 1e6

Example:
Input: [3,2,2,4,2,2]
Output: 2

Explanation:
2 occurs with the frequency of 2 > [6/2] = 3
"""

from collections import Counter

# Less optimal solution
def majority_element(A):
    return Counter(A).most_common(1)[0][0]

# Optimal solution (think in terms of bits)
def major_element(A):
    n = len(A)
    answer = 0
    for bit in range(32):
        ones = 0
        for num in A:
            if (1 << bit) & num:
                ones += 1
        if ones > n // 2:
            answer += (1 << bit)
    return answer

print(majority_element([3,2,2,4,2,2]))
print(major_element([3,2,2,4,2,2]))