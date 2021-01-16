'''
Question -> https://www.hackerrank.com/challenges/recursive-digit-sum/problem
@Author -> Taklemariam Alazar
'''
def recSum(n,k):
    n = str(n)
    if len(n) == 1:
        return n 
    ans = 0
    for i in range(len(n)):
        ans = ans + int(n[i])
    ans = ans * k
    
    return recSum(ans,1)
print(recSum("123", 3))

