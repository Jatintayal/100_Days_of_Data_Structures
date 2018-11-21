#!/bin/python3

import math
import os
import random
import re
import sys

def largestRectangle(h):
    areas = []
    l = len(h)
    for x in range(l - 1):
        for i in range(l - x):
            areas.append((l-x-i) * min(h[i:l-x]))
    return max(areas)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
