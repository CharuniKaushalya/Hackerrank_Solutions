#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    a = p//2
    b = abs(n//2 - p//2)
    return min(a,b)

if __name__ == '__main__':
    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(result)
