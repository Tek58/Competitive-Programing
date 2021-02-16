'''
Question -> https://leetcode.com/problems/flood-fill/
@author -> Taklemariam Alazar
'''

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        visited = set()
        currentColor = image[sr][sc]
        n = len(image)
        m = len(image[0])
        self._helper(image, sr, sc, visited,  newColor, n , m, currentColor)
        return image
        
    def _helper(self, image, sr, sc, visited, newColor, n, m, currentColor):
        visited.add((sr,sc))
        image[sr][sc] = newColor
        
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        for direction in directions:
            new_i = sr + direction[0]
            new_j = sc + direction[1]
            if 0 <= new_i < n and 0 <= new_j < m and image[new_i][new_j] == currentColor:
                new_val = (new_i, new_j)
                if (new_val not in visited):
                    visited.add(new_val)
                    self._helper(image, new_i, new_j, visited, newColor, n, m, currentColor)
