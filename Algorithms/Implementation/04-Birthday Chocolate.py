#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(n, s, d, m):
    count = 0
    for i in range(n):
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
