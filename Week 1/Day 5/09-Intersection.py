'''
Question -> https://leetcode.com/problems/intersection-of-two-arrays/
@Author : Taklemariam Alazar
'''
def intersection(nums1, nums2):
    nums1 = set(nums1)
    nums2 = set(nums2)
    answer = (nums1 and nums2) - (nums2 - nums1) 
    return list(answer)