#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(n, s, d, m):
    # # List comprehention answer
    # countlist = sum([(sum(s[i:i+m]) == d) for i in range(n - m +1)] )
    # print(countlist)
    count = 0
    for i in range(n-m+1):
        if(sum(s[i:i+m]) == d):
            count +=1
    print(count)


if __name__ == '__main__':
    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    birthday(n, s, d, m)
