'''
Question -> https://leetcode.com/contest/weekly-contest-112/problems/most-stones-removed-with-same-row-or-column/
@Author -> Taklemariam Alazar
'''
class Solution:
    def removeStones(self, stones):
        count = [0]
        stone_dict = defaultdict(list)
        visited = set()
        
        row = {} 
        col = {}
        
        for stone in stones:
            r = stone[0]
            c = stone[1]
            
            if r not in row:
                row[r] = [stone]
            else:
                row[r].append(stone)
            
            if c not in col:
                col[c] = [stone]
            else:
                col[c].append(stone)
        
        for stone in stones:
            state = tuple(stone)
            if state not in visited:
                visited.add(state)
                self.dfs(row,col,stone,count,visited)
        
        return count[0]
    
    def dfs(self,row,col,stone,count,visited):  
        state = tuple(stone)
        
        for st in row[state[0]]:
            stState = tuple(st)
            if stState not in visited:
                count[0] += 1
                visited.add(stState)
                self.dfs(row,col,st,count,visited)
        
        for st in col[state[1]]:
            stState = tuple(st)
            if stState not in visited:
                count[0] += 1
                visited.add(stState)
                self.dfs(row,col,st,count,visited)
                
        return count[0]