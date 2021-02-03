'''
Question -> https://leetcode.com/problems/top-k-frequent-elements/
@Author -> Taklemariam Alazar
'''
import heapq
class Solution:
    def topKFrequent(self, nums, k):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        heap = []
        for i in dic:
            heapq.heappush(heap, (-dic[i], i))
        
        result = []
        for i in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result