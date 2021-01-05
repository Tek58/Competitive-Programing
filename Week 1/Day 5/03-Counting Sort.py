'''
@Author : Taklemariam Alazar
Counting Sort Implementation
'''
def countingSort(lis):
    maximum = 0
    for i in range(len(lis)):
        if lis[i] > maximum:
            maximum = lis[i]
    placeHolder = [0]*(maximum + 1)
    
    for i in range(len(lis)):
        placeHolder[lis[i]] += 1

    result = []
    for i in range(len(placeHolder)):
        if placeHolder[i] != 0:
            result += [i]*placeHolder[i]
    return result

print(countingSort([5,17,55,4,8,3,0,1]))