'''
Question -> https://leetcode.com/problems/minimum-time-difference/
@author -> Taklemariam Alazar
'''
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        container = []
        result = []
        for i in timePoints:
            val = i.split(":")
            container.append((int(val[0])*60 + int(val[1])))
        container.sort()
        for i in range(len(container)-1):
            result.append(min(1440 - abs(container[i] - container[i+1]), abs(container[i] - container[i+1])))
        result.append(min(1440 - abs(container[0] - container[-1]), abs(container[0] - container[-1])))
        
        return min(result)