num = [1,1,2]
n = [0,0,1,1,1,2,2,3,3,4]

# remove duplicados e retorna quantos foram removidos
def remove_duplicates(nums):
    i = 1
    while i < len(nums):
        if nums[i] == nums[i-1]:
            del nums[i-1]
        else:
            i += 1
    return i

print(remove_duplicates(n))