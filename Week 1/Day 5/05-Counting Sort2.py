'''
Question -> https://www.hackerrank.com/challenges/countingsort2/problem

@Author : Taklemariam Alazar
Counting Sort Implementation 2
'''
def countingSort(arr):
    maximum = 0
    for i in range(len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    placeHolder = [0]*(maximum + 1)
    
    for i in range(len(arr)):
        placeHolder[arr[i]] += 1

    result = []
    for i in range(len(placeHolder)):
        if placeHolder[i] != 0:
            result += [i]*placeHolder[i]
    return result