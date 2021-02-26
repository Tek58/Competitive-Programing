'''
Question -> https://leetcode.com/problems/sort-array-by-increasing-frequency/
@Author -> Taklemariam Alazar
'''
def frequencySort(self, nums):
    dic = {}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    nums.sort()
    nums = nums[::-1]
    nums.sort(key=lambda x:dic[x])
    return nums