'''
@Author : Taklemariam Alazar
Selection Sort Implementation
'''
def selectionSort(lis):
    for i in range(len(lis)):
        minimum = lis[i]
        index = i
        for j in range(i,len(lis)):
            if minimum > lis[j]:
                minimum = lis[j]
                index = j
        lis[i] , lis[index] = lis[index], lis[i]

    return lis



print(selectionSort([17,2,5,6,3,0,1]))