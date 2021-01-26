'''
Question -> https://leetcode.com/problems/binary-search/submissions/
@Author -> Taklemariam Alazar
'''
def search(nums, target):
        return helper(nums, 0, len(nums)-1, target)
def helper( nums, left, right, target):
    if left <= right:
        mid = (right + left)//2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return helper(nums, mid+1, right, target)
        else:
            return helper(nums, left, mid-1, target)
    return -1