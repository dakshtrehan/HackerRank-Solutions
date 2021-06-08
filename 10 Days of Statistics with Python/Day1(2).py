#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s=[]
    for i in range(len(values)):
        for j in range(freqs[i]):
            s.append(values[i])
    s.sort()
    n=len(s)
    if n%2 != 0:
        x = statistics.median(s[:n//2])
        z = statistics.median(s[n//2+1:])
    else:
        x = statistics.median(s[:n//2])
        z = statistics.median(s[n//2:])

    print("{:.1f}".format(z-x))

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
