def twoSum(x,t):
    for i in range(len(x)):
        for j in range(1,len(x)):
            if x[i] + x[j] == t and i != j:
                print("[",i, ",", j ,"]")
twoSum([2,7,11,15],9)
    
