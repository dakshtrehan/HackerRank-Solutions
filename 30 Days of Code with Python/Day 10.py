#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    Bin = bin(n)
    Bin = Bin[2:]
    j=0
    lis=[0 for k in range (len(Bin))]
    
    for i in range(len(Bin)):
        if Bin[i]=='1':
            lis[j]+=1            
         
        if Bin[i]=='0':
            j+=1
    print(max(lis))
