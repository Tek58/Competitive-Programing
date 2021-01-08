'''
Question -> https://leetcode.com/problems/non-decreasing-array/
@Author : Taklemariam Alazar
'''
def checkPossibility(nums):
    isPossible = False
    changed = 0
    counter = 0
    for i in range(len(nums)-1):
        if (nums[i] - nums[i+1] == -1) or (nums[i+1] - nums[i] == 1):
            counter += 1
            print(nums[i], nums[i+1])
print(checkPossibility([[1,2,3]]))
