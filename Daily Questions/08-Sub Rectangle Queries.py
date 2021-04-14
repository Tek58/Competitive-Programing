'''
Question -> https://leetcode.com/problems/subrectangle-queries/
'''
class SubrectangleQueries:
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle
        self.collection = []

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        self.collection.append([row1, col1, row2, col2, newValue])
        

    def getValue(self, row: int, col: int) -> int:
        for i in range(len(self.collection)-1, -1, -1):
            row1, col1, row2, col2, value = self.collection[i]
            if row1 <= row <= row2 and col1 <= col <= col2:
                return value
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)