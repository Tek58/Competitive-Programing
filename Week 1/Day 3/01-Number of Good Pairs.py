'''
Question -> https://leetcode.com/problems/number-of-good-pairs/
@Author : Taklemariam Alazar
'''
def numberOfGoodPairs(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            if nums[i] == nums[j] and i < j :
                count += 1
    return count
