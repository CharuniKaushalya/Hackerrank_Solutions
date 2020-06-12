#!/bin/python3

import os
import sys
import itertools

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    lis = list(itertools.product(keyboards, drives))
    maxBudget = -1
    for i in lis:
        tot = sum(i)
        if(tot <= b and maxBudget < tot):
            maxBudget = tot
    return maxBudget

if __name__ == '__main__':
    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))


    moneySpent = getMoneySpent(keyboards, drives, b)

    print(moneySpent)
