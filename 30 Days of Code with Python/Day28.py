#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    firstname=[]
    emailid=[]
    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        firstname.append(firstName)

        emailID = firstNameEmailID[1]
        emailid.append(emailID)
        
    dic={key:value for key,value in zip(emailid,firstname) if "@gmail.com" in key}
    for i in sorted(dic.values()):
        print(i)
