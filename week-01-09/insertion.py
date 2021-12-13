#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    last = arr[n - 1]
    for i in range(n-1, -1, -1):
        if i == 0:
            arr[i] = last
            
        elif last > arr[i - 1]:
            arr[i] = last
            for i in arr:
                print(i, end=" ")
            print()
            break
        else:
            arr[i] = arr[i - 1]
        for i in arr:
            print(i, end=" ")
        print()
            
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
