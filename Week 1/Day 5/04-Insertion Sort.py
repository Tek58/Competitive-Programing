'''
@Author : Taklemariam Alazar
Insertion Sort IMplementation
'''
def insertionSort(lis):
    for i in range(len(lis)):
        j = i
        while j > 0 and lis[j-1] > lis[j] :
            lis[j-1], lis[j] = lis[j] , lis[j-1]
            j -=1
        
    return lis
print(insertionSort([9,5,1,0,7,3,5,4]))