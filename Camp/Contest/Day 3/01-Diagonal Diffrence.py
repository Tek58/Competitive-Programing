'''
Question -> https://www.hackerrank.com/contests/a2sv-contest-8/challenges/diagonal-difference
@author -> Taklemariam Alazar
'''
def diagonalDifference(arr):
    right, left = 0 , 0
    for i in range(len(arr)):
        right += arr[i][i]
        left += arr[i][len(arr)-i-1]
    return abs(right - left)