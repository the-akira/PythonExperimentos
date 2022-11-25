"""
There is a row of empty (.) and filled (x) seats.

Find the minimum number of moves required to make the people sit together.

Constraints:
- 1 <= N <= 1e6

Example:
Input: "..x..x."
Output: 2

Explanation:
Either of the "x"s can move to the seat closest to the other one.

"..xx..." OR "....xx."
"""

def minimum_moves(A):
    MOD = 10000003

    crosses = [i for i, c in enumerate(A) if c == "x"]
    crosses = [(cross - i) for i, cross in enumerate(crosses)]

    n = len(crosses)

    if n == 0:
        return 0

    answer = float('inf')
    segment_start = crosses[n//2]
    total = 0
    for cross in crosses:
        total += abs(cross - segment_start)
        total %= MOD
    answer = min(answer, total % MOD)

    return answer

print(minimum_moves(".x..x..xx."))