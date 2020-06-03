import os
import sys
import time

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    return time.strftime('%H:%M:%S', time.strptime(s , '%I:%M:%S%p'))

if __name__ == '__main__':
    s = input()
    result = timeConversion(s)
    print(result)