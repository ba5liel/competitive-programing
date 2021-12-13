#!/bin/python3

import math
import os
import random
import re
import sys

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count = 0
    for i in range(len(a)):
    
      for j in range(len(a) - 1):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[j + 1]:
            swap(a, j, j + 1)
            count = count + 1
    print(f'Array is sorted in {count} swaps.')
    print(f'First Element: {a[0]}')
    print(f'Last Element: {a[len(a) - 1]}')

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
