"""
Given an array A of a random permutation of numbers from 1 to N.
Given B, the number of swaps in A that we can make.

Find the largest permutation possible.

Constraints:
- 1 <= N <= 1e6
- 1 <= B <= 1e9

Example:
Input: A = [1,3,2], B = 1
Output: [3,1,2] -> 312

Explanation:
N = 3
Since we can make B = 1 swaps, we swap 1 and 3
"""

def largest_permutation(A, B):
    i = 0
    maximum = len(A)
    d = {x: i for i, x in enumerate(A)}

    while B and i < len(A):
        j = d[maximum]
        if i == j:
            pass
        else:
            B -= 1
            A[i], A[j] = A[j], A[i]
            d[A[i]], d[A[j]] = d[A[j]], d[A[i]]
        i += 1
        maximum -= 1
    return A

print(largest_permutation([3,2,4,1,5],3))
print(largest_permutation([1,3,2],1))