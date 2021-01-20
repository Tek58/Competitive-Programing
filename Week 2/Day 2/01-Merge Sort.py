'''
Question -> implement Merge Sort
@Author -> Taklemariam Alazar
'''
from random import randint
def random(size, max):
    return [randint(-1 * max, max) for _ in range(size)]

def combine(ans1, ans2):
    i,j = 0 , 0
    combined = []
    while i < len(ans1) and j < len(ans2):
        if ans1[i] <= ans2[j]:
            combined.append(ans1[i])
            i += 1
        else:
            combined.append(ans2[j])
            j += 1
    return combined + ans1[i:] + ans2[j:]
def merge(arr):
    start = 0
    end = len(arr) 
    if len(arr) <= 1 :
        return arr
    mid = (start + end) // 2
    ans1 = merge(arr[:mid])
    ans2 = merge(arr[mid:])
    return combine(ans1,ans2)

rand = random(10, 50)
print(merge(rand))