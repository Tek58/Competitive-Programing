'''
Question -> https://leetcode.com/problems/employee-importance/
@Author -> Taklemariam Alazar
'''
"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        container = defaultdict()
        for i in employees:
            container[i.id] = i
        return self.dfs(container, id)
    
    def dfs(self, container, id):
        employee = container[id]
        imp = container[id].importance

        for i in employee.subordinates:
            self.dfs(container, i)
            
        return imp