#!/bin/python3

import math
import os
import random
import re
import sys
import string

# Complete the designerPdfViewer function below.
def designerPdfViewer(h, word):
    maxl = 0
    for i in word:
        weight = h[ord(i) - 97]
        print(weight)
        if maxl < weight :
            maxl = weight
        print(maxl)
    return len(word)*maxl

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    print(result)
