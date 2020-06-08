#!/bin/python3
"""
Solve https://www.hackerrank.com/challenges/migratory-birds/problem
"""

# Complete the migratoryBirds function below.
def migratory_birds(arr):
    return max(set(arr), key=arr.count) 

if __name__ == '__main__':

    arr_count = int(input().strip())

    bird_arr = list(map(int, input().rstrip().split()))

    result = migratory_birds(bird_arr)

    print(result)
