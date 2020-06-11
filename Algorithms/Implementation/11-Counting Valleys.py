#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the countingValleys function below.
def countingValleys(n, s):
    level=valley=0
    for i in range(n):
        if(s[i]=='U'):
            level+=1
            if(level==0):
                valley+=1
        else:
            level-=1
    
    print(valley)

if __name__ == '__main__':
    n = int(input())

    s = input()

    countingValleys(n, s)
