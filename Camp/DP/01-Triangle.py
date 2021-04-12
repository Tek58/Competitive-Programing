'''
Question -> https://leetcode.com/problems/triangle/
@Author -> Taklemariam Alazar
'''
# Bottom Up
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        container = triangle[len(triangle)-1]
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                container[j] = triangle[i][j] + (min(container[j], container[j+1]))
        
        return container[0]
            
# Top Down
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        return self.dfs(0,0,triangle, memo)
    
    def dfs(self, row, col, triangle, memo):
        if row == len(triangle)-1:
            return triangle[row][col]
        if (row, col) in memo:
            return memo[(row, col)]
        
        val1 = self.dfs(row+1, col, triangle, memo)
        val2 = self.dfs(row+1, col+1, triangle, memo)        
        
        result = min(val1, val2) + triangle[row][col]
        
        memo[(row, col)] = result 
        return result