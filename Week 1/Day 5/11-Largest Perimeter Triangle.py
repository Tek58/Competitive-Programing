'''
Question -> https://leetcode.com/problems/largest-perimeter-triangle/
@Author : Taklemariam Alazar
'''
def largestPerimeterTriangle(A):
    A = sorted(A)
    a =  []
    a.sort
    for i in range(1,len(A)-1):
        last_element, second_last, third_last = A[-i], A[-i-1], A[-i-2]
        if last_element <  (second_last + third_last):
            return last_element + second_last + third_last
        if len(A) <= 3:
            break
    return 0