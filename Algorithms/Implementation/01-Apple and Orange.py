#!/bin/python3

import math
import os
import random
import re
import sys
# print(sum(s <= a + i <= t for i in apple))
# print(sum(s <= b + i <= t for i in orange))

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, m, n, apples, oranges):
    counta = 0
    countb = 0
    for i in apples:
        if i+a in range(s,t+1):
            counta = counta+1
    for j in oranges:
        if j+b in range(s,t+1):
            countb = countb +1    
    print(counta)
    print(countb)      

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, m,n, apples, oranges)
