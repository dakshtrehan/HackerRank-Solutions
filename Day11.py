#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    global_max = -sys.maxsize - 1
    
    for row in range(len(arr)-2):
        for col in range(len(arr[0])-2):
            
            hourglass = []
            hourglass.extend(arr[row][col:col+3])
            hourglass.append(arr[row+1][col+1])
            hourglass.extend(arr[row+2][col:col+3])
            
            if sum(hourglass) > global_max:
                global_max = sum(hourglass)
                
    print(global_max)
