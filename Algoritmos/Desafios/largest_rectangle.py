"""
Given an array heights that contains the height of each
bar in the histogram, and we are asked to return the area
of the largest rectangle in the histogram. Note that each
bar has a width of 1.

Exemplo:

Input:

heights = [3,2,4,5,7,6,1,3,8,9,11,10,7,5,2,6]

Output: 35
"""

# 1st solution
def largest_rectangle(heights):
    max_area = 0
    for i in range(len(heights)):
        left = i
        while left - 1 >= 0 and heights[left-1] >= heights[i]:
            left -= 1
        right = i
        while right + 1 < len(heights) and heights[right+1] >= heights[i]:
            right += 1
        max_area = max(max_area, heights[i] * (right-left+1))
    return max_area

print(largest_rectangle([3,2,4,5,7,6,1,3,8,9,11,10,7,5,2,6]))

# 2nd solution
def recursive(heights, low, high):
    if low > high:
        return 0
    elif low == high:
        return heights[low]
    else:
        minh = min(heights[low:high+1])
        pos_min = heights.index(minh, low, high+1)
        from_left = recursive(heights, low, pos_min-1)
        from_right = recursive(heights, pos_min+1, high)
        return max(from_left, from_right, minh *(high-low+1))

def find_largest_rectangle(heights):
    return recursive(heights, 0, len(heights)-1)

print(find_largest_rectangle([3,2,4,5,7,6,1,3,8,9,11,10,7,5,2,6]))

# 3rd solution
def find_rectangle_largest(heights):
    heights = [-1] + heights + [-1]
    from_left = [0] * len(heights)
    stack = [0]
    for i in range(1, len(heights)-1):
        while heights[stack[-1]] >= heights[i]:
            stack.pop()
        from_left[i] = stack[-1]
        stack.append(i)
    from_right = [0] * len(heights)
    for i in range(1, len(heights)-1)[::-1]:
        while heights[stack[-1]] > heights[i]:
            stack.pop()
        from_right[i] = stack[-1]
        stack.append(i)
    max_area = 0
    for i in range(1, len(heights)-1):
        max_area = max(max_area, heights[i]*(from_right[i]-from_left[i]-1))
    return max_area

print(find_rectangle_largest([3,2,4,5,7,6,1,3,8,9,11,10,7,5,2,6]))

def rectangle_larget(heights):
    heights = [-1] + heights + [-1]
    max_area = 0
    stack = [(0, -1)]
    for i in range(1, len(heights)):
        start = i
        while stack[-1][1] > heights[i]:
            top_index, top_height = stack.pop()
            max_area = max(max_area, top_height*(i-top_index))
            start = top_index
        stack.append((start, heights[i]))
    return max_area

print(rectangle_larget([3,2,4,5,7,6,1,3,8,9,11,10,7,5,2,6]))