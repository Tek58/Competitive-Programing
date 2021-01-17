<<<<<<< HEAD
'''
Question -> https://leetcode.com/problems/fibonacci-number/
@Author : Taklemariam Alazar
'''
'''
Iteration implementatio
def fib(x):
    if x <= 1:
        return 1
    num1 = 1
    num2 = 1
    for i in range(1,x):
        temp = num2
        num2 = num1 + num2
        num1 = temp
    return num2
'''
#Recursive Implementation
def fib(self, n: int) -> int:
    if n <= 1:
        return n
    else:
        return (self.fib((n-2)) + self.fib((n-1)))
