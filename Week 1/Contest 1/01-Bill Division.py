#Question -> https://www.hackerrank.com/contests/a2sv2/challenges/bon-appetit
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill = list(bill)
    summ = 0
    for i in range(len(bill)):
        summ += int(bill[i])
    result = summ - bill[k]
    if result//2 == b:
        print("Bon Appetit")
    else:
        charged = b - result//2
        print(charged)
    

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
