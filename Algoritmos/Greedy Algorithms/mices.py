"""
There are N mices and N holes.
A mice takes 1 minute to travel 1 unit left or right.

Find the minimum time after which all mice are in holes.

Constraints:
- 1 <= N <= 1e5
- -1e9 <= A[i] <= B[i] <= 1e9

Example:
Input: A = [3,2,-4], B = [0,-2,4]
Output: 2

Explanation:
-4 -> -2: 2
2  ->  0: 2
3  ->  4: 1
"""

def minimum_time(A, B):
    A.sort(), B.sort()

    answer = 0
    for a, b in zip(A, B):
        answer = max(answer, abs(a-b))
    return answer

print(minimum_time([3,2,-4], [0,-2,4]))