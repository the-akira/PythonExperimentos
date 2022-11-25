"""
Given a list of intervals: [start, end] for meetings.

Find the least number of meeting rooms required.

Constraints:
- 1 <= N <= 1e5
- 1 <= A[i][0] <= A[i][1] <= 1e9

Example:
Input: [[5,10],[15,10],[0,30]]
Output: 2

Explanation:
[0,30] and [5,10] take place simultaneously.
Same for [0,30] and [15,20]
"""

def least_meeting_rooms(array):
    data = []
    for start, end in array:
        data.append((start, 1))
        data.append((end, -1))
    data.sort()
    curr, answer = 0, 0
    for _, v in data:
        curr += v
        answer = max(answer, curr)
    return answer

print(least_meeting_rooms([[5,10],[15,20],[0,30]]))