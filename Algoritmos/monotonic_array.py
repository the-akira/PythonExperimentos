# Dado um array de inteiros, determine se o array é monotônico ou não.

"""
Uma array é monotônico se e somente se for monotôno aumentando ou diminuindo
"""

A = [6,5,4,4,3] 
B = [1,1,1,3,3,4,3,2,4,2]
C = [1,1,2,3,7]

def solution(nums): 
    return (all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or 
            all(nums[i] >= nums[i + 1] for i in range(len(nums) - 1))) 
  
print(solution(A)) 
print(solution(B)) 
print(solution(C)) 