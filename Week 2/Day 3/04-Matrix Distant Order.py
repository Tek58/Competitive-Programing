'''
Question -> https://leetcode.com/problems/matrix-cells-in-distance-order/
@Author -> Taklemariam Alazar
'''
def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        matrix = []
        for i in range(R):
            for j in range(C):
                matrix.append([i,j,abs(i-r0) + abs(j-c0)])
        return [x[:2] for x in sorted(matrix,key=lambda x: x[2])]