#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    min = scores[0]
    max = scores[0]
    min_count = 0
    max_count = 0
    for i in scores[1:]:
        if i>max:
            max = i
            max_count += 1
        if i<min:
            min = i
            min_count += 1
    print(max_count,min_count)

if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    breakingRecords(scores)
