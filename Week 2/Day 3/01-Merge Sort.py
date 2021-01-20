'''
Question -> https://leetcode.com/problems/sort-an-array/
@Author -> Taklemariam Alazar
'''
def combine(ans1, ans2):
    i,j = 0 , 0
    combined = []
    ans1 = list(ans1)
    ans2 = list(ans2)
    while i < len(ans1) and j < len(ans2):
        if ans1[i] <= ans2[j]:
            combined.append(ans1[i])
            i += 1
        else:
            combined.append(ans2[j])
            j += 1
    return combined + ans1[i:] + ans2[j:]

def sortArray( arr):
    start = 0
    end = len(arr) 
    if len(arr) <= 1 :
        return arr
    mid = (start + end) // 2
    ans1 = sortArray(arr[:mid])
    ans2 = sortArray(arr[mid:])
    return combine(ans1,ans2)