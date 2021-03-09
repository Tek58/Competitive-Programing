'''
Question -> https://leetcode.com/problems/n-th-tribonacci-number/
@Author -> Taklemariam Alazar
'''
def tribonacci(self, n: int) -> int:
    container = [0]*38
    container[1] = 1
    container[2] = 1
    for i in range(3,len(container)):
        Sum = 0
        for j in range(i-1,i-4,-1):
            Sum += container[j]
        container[i] = Sum
    return container[n]