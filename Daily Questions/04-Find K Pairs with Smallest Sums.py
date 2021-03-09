'''
Question -> https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
@Author -> Taklemariam Alazar
'''
import heapq as heap
class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if (not nums1 and not nums2) or (not nums1 or not nums2):
            return 
        store = []
        result = []
        for i in nums1:
            for j in nums2:
                heap.heappush(store, (i+j,i,j))
        validator  = True
        counter = 0
        while validator:
            if store and counter < k:
                poped_value = heap.heappop(store)
                result.append(list(poped_value[1:]))
                counter +=1
            else:
                validator = False 
        return result