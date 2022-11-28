"""
Given and array of integers arr and integer k,
find the kth largest element.

Restrição: 1 <= k <= |arr|

Exemplo:

Input:

arr = [4,2,9,7,5,6,7,1,3]
k = 4

Output: 6

Explicação:

1st largest element is 9
2nd largest element is 7
3rd largest element is 7
4th largest element is 6
"""

# 1st solution
def kth_largest(arr, k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)

print(kth_largest([4,2,9,7,5,6,7,1,3],4))

# 2nd solution
def kth_larget_element(arr, k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

print(kth_larget_element([4,2,9,7,5,6,7,1,3],4))

# 3rd solution
import heapq

def find_kth_larget(arr, k):
    arr = [-element for element in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

print(find_kth_larget([4,2,9,7,5,6,7,1,3],4))