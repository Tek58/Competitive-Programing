'''
Question -> https://www.hackerrank.com/challenges/find-the-median/problem
@Author : Taklemariam Alazar

'''
def findMedian(arr):
    sorted_arr = sorted(arr)
    median = 0
    length = len(sorted_arr)
    if length % 2 == 0:
        median = (sorted_arr[(length//2)] + sorted_arr[(length//2)-1])/2
    else:
        median = sorted_arr[(length//2)]
    return median
