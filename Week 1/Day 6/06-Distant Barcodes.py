'''
Question -> https://leetcode.com/problems/distant-barcodes/
@Author -> Taklemariam Alazar
'''
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = [0]* (max(barcodes)+1)
        for i in barcodes:
            counter[i] += 1
        heap = []
        for i in range(len(counter)):
            if counter[i] != 0:
                heapq.heappush(heap, (-counter[i], i))
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
                result.append(heapq.heappop(heap)[1])
            
        return result