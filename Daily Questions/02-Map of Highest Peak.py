'''
Question -> https://leetcode.com/problems/map-of-highest-peak/
@Author -> Taklemariam Alazar
'''
from collections import deque
class Solution:
    def highestPeak(self, isWater):
        visited = set()
        queue = deque()
        adjacents = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(len(isWater)):
            for j in range(len(isWater[0])):
                if isWater[i][j] == 1:
                    visited.add((i,j))
                    queue.append((i,j))
                    isWater[i][j] = 0
        while queue:
            result = queue.popleft()
            new_i = result[0]
            new_j = result[1]
            for adj in adjacents:
                new_row = new_i + adj[0]
                new_col = new_j + adj[1]
                if (self.validate(new_row, new_col, isWater, visited)):
                    visited.add((new_row, new_col))
                    queue.append((new_row, new_col))
                    isWater[new_row][new_col] = isWater[new_i][new_j] + 1
        return isWater
    
    def validate(self,row, col, isWater, visited):
        if (0 <= row < len(isWater)) and (0 <= col < len(isWater[0])) and ((row, col) not in visited):
            return True
        return False