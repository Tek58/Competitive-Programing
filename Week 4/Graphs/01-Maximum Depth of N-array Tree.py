'''
Question -> https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
@Author -> Taklemariam Alazar
'''

# Definition for a Node. and BFS Soln
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

from collections import deque
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        queue = deque()
        if not root:
            return 0
        depth = 1
        queue.append((root,depth))
        while queue:
            current, new_depth = queue.popleft()
            depth = max(depth, new_depth)
            for child in current.children:
                queue.append((child, new_depth + 1))
        return depth
    
'''
# DFS soln
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        depth = 0
        for child in root.children:
            depth = max(self.maxDepth(child), depth)
        return depth +1
'''