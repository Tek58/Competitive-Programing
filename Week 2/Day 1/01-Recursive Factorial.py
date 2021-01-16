''''
Question -> https://www.hackerrank.com/challenges/30-recursion/problem
@Author -> Taklemariam Alazar
'''
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))
print(factorial(1000))