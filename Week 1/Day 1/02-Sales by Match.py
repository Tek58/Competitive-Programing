def SBM(n,ar):
    count = 0
    lis = [0]*101
    for i in ar:
        ar.count(i)
        lis[i-1] += 1
    for i in range(len(cum)):
        if lis[i] != 0:
            count += lis[i] // 2
    return count
print(SBM(9,[10,20,20,10,10,30,50,10,20]))
