'''
Question -> https://leetcode.com/problems/reorganize-string/
@Author : Taklemariam Alazar
'''
def reorganizeString(S):
    storage  = [0]*26
    for i in S:
        storage[(ord(i)-97)] += 1
    Max = storage[0]   
    Sum = 0
    index = 0
    for i in range(len(storage)):
        Sum += storage[i] 
        if storage[i] > Max:
            Max = storage[i]
            index = i
    reorganized = ''
    if Max == 1 or Max == 0 or Max > (len(S)//2) + 1:
        return ' " " '
    for i in range(len(storage)):
        for j in range(len(storage)):
               pass 




 
    return storage
print(reorganizeString("abaa"))