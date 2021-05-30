# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
n=int(input())
for i in range(n):
    t=int(input())
    if t==1:
        print("Not prime")
    elif t==2:
        print("Prime")   
    else:
        f=0
        for j in range(2,int(math.sqrt(t))+1):
            if t%j==0:
                f=1
                break
        if f==1:
            print("Not prime")
        else:
            print("Prime")
