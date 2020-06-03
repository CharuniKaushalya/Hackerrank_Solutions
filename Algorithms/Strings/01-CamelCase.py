#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    splitted = re.sub('([A-Z]+)', r' \1', s).split()
    return len(splitted)

if __name__ == '__main__':
     s = input()

    result = camelcase(s)

    print(str(result))
