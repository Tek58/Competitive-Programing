'''
Question -> https://leetcode.com/contest/weekly-contest-174/problems/jump-game-v/
@Author -> Taklemariam Alazar
'''
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        memo = {}
        maxResult = 1
        for i in range(len(arr)):
            maxResult = max(maxResult, self.dfs(i, arr, memo, d))
        return maxResult
    
    def dfs(self, i, arr, memo, d):
        if i not in memo:
            value = 0
            j = 1
            while j <= d and 0 <= i+j < len(arr) and arr[i+j] < arr[i]:
                value = max(value, self.dfs(i+j, arr, memo, d))
                j += 1
                
            k = 1
            while k <= d and 0 <= i-k < len(arr) and arr[i-k] < arr[i]:
                value = max(value, self.dfs(i-k, arr, memo, d))
                k += 1
            memo[i] = value + 1
        return memo[i]