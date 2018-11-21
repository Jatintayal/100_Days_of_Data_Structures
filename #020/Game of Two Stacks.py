#!/bin/python3

import os
import sys

def twoStacks(x, a, b):
    sum = 0
    score = 0       
    while(x > sum + a[-1] or x > sum + b[-1]):
        if a[-1] >= b[-1]:
            sum += b[-1]
            b.pop(-1)
        else:
            sum += a[-1]
            a.pop(-1)
        score += 1
    return score

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input())

    for g_itr in range(g):
        nmx = input().split()

        n = int(nmx[0])

        m = int(nmx[1])

        x = int(nmx[2])

        a = list(map(int, reversed(input().rstrip().split(' '))))
        b = list(map(int, reversed(input().rstrip().split(' '))))

        result = twoStacks(x, a, b)

        fptr.write(str(result) + '\n')

    fptr.close()
