'''
Question -> https://leetcode.com/problems/find-pivot-index/
@author -> Taklemariam Alazar
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix  = [nums[0]]
        postfix = [nums[-1]]
        for i in range(1, len(nums)):
            prefix.append(prefix[i-1] + nums[i])
            postfix.append(postfix[i-1] + nums[len(nums)-1 - i])
        
        for i in range(len(nums)):
            if prefix[i] == postfix[len(nums)-1-i]:
                return i
        return -1