'''
Question -> https://leetcode.com/contest/weekly-contest-174/problems/reduce-array-size-to-the-half/
@Author -> Taklemariam Alazar
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        container = dict()
        temp = []
        for i in arr:
            if i not in container:
                container[i] = 1
            else:
                container[i] += 1
                
        for i in container.values():
            temp.append(i)
            
        temp.sort(reverse=True)
        totalSum = 0
        value = len(arr) // 2
        
        for i in range(len(temp)):
            totalSum += temp[i]
            if totalSum >= value:
                return i + 1