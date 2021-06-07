#!/bin/python3

import math
import os
import random
import re
import sys
import statistics

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
    # Write your code here
    n=len(arr)
    arr=sorted(arr)
    left_arr= arr[:int((len(arr)/2))] if n%2==0 else arr[:int((len(arr)/2))]
    right_arr= arr[int((len(arr)/2)):] if n%2==0 else arr[int((len(arr)/2)+1):]
    
    median_arr = statistics.median(arr)
    left_median_arr = statistics.median(left_arr)
    right_median_arr = statistics.median(right_arr)
    
    return int(left_median_arr), int(median_arr), int(right_median_arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
