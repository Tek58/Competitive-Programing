'''
Question -> https://leetcode.com/problems/k-closest-points-to-origin/
@Author : Taklemariam Alazar
'''
import math
def kClosest(points, k):
    value = []
    returned = []
    for j in range(len(points)):
        distance = math.sqrt((points[j][1])**2 + (points[j][0])**2)
        index_val = [distance, j]
        value.append(index_val )
    value = sorted(value)
    for i in range(k):
        returned.append(points[value[i][1]])
    return returned