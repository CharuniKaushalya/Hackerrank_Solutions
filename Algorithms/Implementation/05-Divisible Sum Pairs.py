#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import combinations 

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    comb = combinations(ar, 2)
    print(sum([sum(i) % k == 0 for i in comb]))


if __name__ == '__main__':
    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    divisibleSumPairs(n, k, ar)

