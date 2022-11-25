"""
N kids stand in a line, each having an integer rating.

We distribute candies following:
- Each kid gets at least 1 candy
- Kids with higher ratings than their neighbours get more candies

Find the maximum candies required.

Constraints:
- 1 <= N <= 1e5

Example:
Input: [1,3,7,1]
Output: 7

Explanation:
Candies: [1,2,3,1] = 7
"""

def maximum_candies(array):
    n = len(array)
    data = sorted((x,i) for i, x in enumerate(array))

    candies = [1] * n

    for _, i in data:
        if i > 0 and array[i] > array[i-1]:
            candies[i] = max(candies[i], candies[i-1] + 1)
        if i < n - 1 and array[i] > array[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)

    return sum(candies)

print(maximum_candies([1,3,7,1]))