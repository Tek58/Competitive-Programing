'''
Question -> https://leetcode.com/contest/weekly-contest-156/problems/unique-number-of-occurrences/
@Author -> Taklemariam Alazar
'''
class Solution:
    def uniqueOccurrences(self, arr):
        dict = {}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        lis = []
        for i in dict:
            lis.append(dict[i])
        newLis = set(lis)
        return len(lis) == len(newLis)