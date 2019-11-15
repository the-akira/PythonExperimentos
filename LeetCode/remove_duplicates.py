num = [1,1,2]
n = [0,0,1,1,1,2,2,3,3,4]

def remove(nums):
	i = 1
	while i < len(nums):
		if nums[i] == nums[i-1]:
			del nums[i-1]
		else:
			i += 1
	return i

print(remove(n))