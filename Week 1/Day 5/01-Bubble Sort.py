'''
@Author : Taklemariam Alazar
Bubble Sort Implementation 
'''
def bubbleSort(lis):
    for j in range(len(lis)):
        for i in range(len(lis)-1):
            if lis[i] > lis[i+1]:
                lis[i], lis[i+1] = lis[i+1], lis[i]
    return lis
print(bubbleSort([17,2,5,5,6,3,0,1]))