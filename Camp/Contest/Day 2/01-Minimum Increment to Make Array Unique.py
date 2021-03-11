'''
Question -> https://leetcode.com/contest/weekly-contest-112/problems/minimum-increment-to-make-array-unique/
@Author -> Taklemariam Alazar
'''
class Solution:
    def minIncrementForUnique(self, A):
        if not A:
            return 0
        A.sort()
        counter = 0
        for i in range(len(A)-1):
            if A[i] == A[i+1] or A[i] > A[i+1]:
                counter += A[i]+1 - A[i+1]
                A[i+1] = A[i] + 1
        return counter