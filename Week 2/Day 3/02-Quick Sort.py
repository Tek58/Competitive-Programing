'''
Question -> https://www.hackerrank.com/challenges/quicksort1/problem
@Author -> Taklemariam Alazar
'''
def quickSort(arr):
    if len(arr) <= 1:
            return arr
    left_arr = []
    right_arr = []
    point = arr[0]
    i = 1
    while i < len(arr):
        if arr[i] < point:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])
        i += 1
    return quickSort(left_arr) + [point] + quickSort(right_arr)