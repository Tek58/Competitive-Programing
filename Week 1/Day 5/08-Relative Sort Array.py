'''
Question -> https://leetcode.com/problems/relative-sort-array/
@Author : Taklemariam Alazar

'''
def relativeSortArray(arr1, arr2):
    maximum = 0
    for i in range(len(arr1)):
        if arr1[i] > maximum:
            maximum = arr1[i]
    placeHolder = [0]*(maximum + 1)

    for i in range(len(arr1)):
        placeHolder[arr1[i]] += 1
    sorted_arr = []
    for i in range(len(arr2)):
        for j in range(len(arr1)):
            if arr1[j] == arr2[i]:
                sorted_arr.append(arr2[i])
                placeHolder[arr1[j]] = 0
    for i in range(len(placeHolder)):
        if placeHolder[i] != 0 :
            sorted_arr += [i]*placeHolder[i]
    return sorted_arr