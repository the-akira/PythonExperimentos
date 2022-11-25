"""
Given a list of intervals: [start, end].

Find the length of the maximal set of mutually disjoint intervals.

Constraints:
- 1 <= N <= 1e5
- 1 <= A[i][0] <= A[i][1] <= 1e9

Example:
Input: [[1,2],[2,10],[4,6]]
Output: 2

Explanation:
Select [1,2] and [4,6].
Selecting [2,10] will block [1,2] and [4,6].
"""

def disjoint_intervals(array):
    array.sort(key=lambda x: x[1])
    prev_start, prev_end = array[0]
    count = 1
    for start, end in array:
        if start <= prev_start:
            pass
        else:
            prev_start, prev_end = start, end
            count += 1
    return count

print(disjoint_intervals([[1,2],[2,10],[4,6]]))