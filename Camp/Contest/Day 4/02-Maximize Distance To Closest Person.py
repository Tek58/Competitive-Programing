'''
Question -> https://leetcode.com/contest/weekly-contest-88/problems/maximize-distance-to-closest-person/
@author -> Taklemariam Alazar
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        first = 0
        second = 1
        result = 0
        while second < len(seats):
            if seats[second] != 1:
                second += 1
            else:
                if first == 0 and seats[first] != 1:
                    result = max(result, second)
                else:
                    val = (second - first)//2
                    result = max(result, val)
                first = second
                second += 1
                
        if seats[second-1] != 1:
            result = max(result, (len(seats)-1 - first))
            
        return result 