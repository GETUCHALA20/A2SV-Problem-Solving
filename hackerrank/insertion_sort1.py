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
    res = []
    for i in range(len(arr)-1,1,-1):
        currentvalue = arr[i]
        position = i
        while position > 0 and arr[position-1] > currentvalue:
            arr[position] = arr[position-1]
            position = position - 1
            val = arr[:]
            res.append(val)
        arr[position] = currentvalue
    res.append(arr)
    for elem in res:
        print(" ".join(map(str,elem)))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
