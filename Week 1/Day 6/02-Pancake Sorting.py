'''
Question -> https://leetcode.com/problems/pancake-sorting/
@Author : Taklemariam Alazar
'''
def maximum(arr):
    Max = arr[0]
    for i in range(len(arr)):
        if arr[i] > Max:
            Max = arr[i]
    return Max
def pancakeSort(arr):
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return []
    value = []
    k = 0
    for i in range(len(arr)):
        if len(arr) > 1:
            max_num = maximum(arr)
            index = arr.index(max_num)
            sorted_arr = arr[(index) + 1 :]
            fliped_arr = arr[:(index)+1]
            fliped_arr = fliped_arr[::-1]
            k = index + 1
            if k > 1:
                value.append(k)
            arr = fliped_arr + sorted_arr
            arr = arr[::-1]
            k = len(arr)
            value.append(k)
            arr = arr[:len(arr)-1] 
    return value
