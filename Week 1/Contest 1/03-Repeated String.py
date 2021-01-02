#Question -> https://www.hackerrank.com/contests/a2sv2/challenges/repeated-string
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repitition = n//len(s)
    remindr = n%len(s)
    count = s.count("a") * repitition
    count_rem = 0
    for i in range(remindr):
        if s[i] == "a":
            count_rem += 1
    return count + count_rem

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
