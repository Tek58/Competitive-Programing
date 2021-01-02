def twoSum(nums, target):
    value = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target and i != j:
                value.append(i)
                value.append(j)
    return list(set(value))
print(twoSum([3,2,4], 6))  

