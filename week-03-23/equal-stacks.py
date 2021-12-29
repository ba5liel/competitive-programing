#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def sumOfArray(arr):
    sum = 0
    for a in arr:
        sum = sum + a
    return sum

def equalStacks(h1, h2, h3):
    # Write your code here
    stacks = [h1, h2, h3]
    minS = sumOfArray(stacks[0])
    
    i = 1
    
    while True:
        if sumOfArray(stacks[i]) > minS:
            stacks[i].pop(0)
            minS = min(sumOfArray(stacks[i]), minS)
            
        elif sumOfArray(stacks[i]) < minS:
            minS = sumOfArray(stacks[i])
           
        elif i == 2 and sumOfArray(stacks[i]) == minS:
            break
        i = (i + 1) % 3
    
    return minS

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
