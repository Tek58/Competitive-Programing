'''
Question -> https://leetcode.com/problems/sort-colors/
@Author -> Taklemariam Alazar
'''
def sortColor(nums):
    curr = 0
    left = 0
    right = len(nums) -1
    while curr <= right:
        if nums[curr] == 2:
            nums[curr], nums[right] = nums[right] , nums[curr]
            right -= 1
        elif  nums[curr] == 0:
            nums[left], nums[curr] = nums[curr] , nums[left]
            left += 1
            curr += 1
        else:
            curr += 1
    return nums