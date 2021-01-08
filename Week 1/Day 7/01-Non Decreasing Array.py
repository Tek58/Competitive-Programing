'''
Question -> https://leetcode.com/problems/non-decreasing-array/
@Author : Taklemariam Alazar
'''

def checkPossibility(nums):
    isPossible = False
    for i in range(len(nums)-1):
        if nums[i] <= nums[i+1]:
            isPossible = True
            print(isPossible)
print(checkPossibility([[4,2,3]]))
