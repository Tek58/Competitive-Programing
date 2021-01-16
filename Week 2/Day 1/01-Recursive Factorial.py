<<<<<<< HEAD
''''
Question -> https://www.hackerrank.com/challenges/30-recursion/problem
@Author -> Taklemariam Alazar
'''
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))
=======
''''
Question -> https://www.hackerrank.com/challenges/30-recursion/problem
@Author -> Taklemariam Alazar
'''
def factorial(n):
    if n == 0:
        return 1
    return (n*factorial(n-1))
>>>>>>> bb2ff047a22035d1a95a4b9d0227fc985a5eabbe
print(factorial(1000))