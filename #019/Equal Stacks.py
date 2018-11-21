#!/bin/python3

import os
import sys

def equalStacks(h1, h2, h3):
    h1.reverse()
    h2.reverse()
    h3.reverse()
    h = [sum(h1), sum(h2), sum(h3)]
    while(not(h[1:] == h[:-1])):
        idx = h.index(max(h))
        print(h, idx)
        if idx == 0:
            temp = h1.pop(-1)
            h[0] -= temp
        elif idx == 1:
            temp = h2.pop(-1)
            h[1] -= temp
        else:
            temp = h3.pop(-1)
            h[2] -= temp
        print(h, idx)
    return h[0]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
