'''
Question -> https://leetcode.com/problems/reorganize-string/
@Author : Taklemariam Alazar
'''
import heapq
class Solution:
    def reorganizeString(self, S: str):
        if len(S) == 1:
            return S

        counter  = [0]*26
        for i in S:
            counter[(ord(i)-97)] += 1
        heap = []
        for i in range(len(counter)):
            if counter[i] != 0:
                heapq.heappush(heap, (-counter[i], chr(i+97)))
        result = []
        while len(heap) > 0:
            if len(heap) > 1:
                x = heapq.heappop(heap)
                y = heapq.heappop(heap)
                result.append(x[1])
                result.append(y[1])
                if x[0] < -1:
                    heapq.heappush(heap, ((x[0])+1, x[1]))
                if y[0] < -1:
                    heapq.heappush(heap, ((y[0])+1, y[1]))
            else:
                x = heapq.heappop(heap)
                if x[0] < -1:
                    return ""
                else:
                    result.append(x[1])
            
        return "".join(result)