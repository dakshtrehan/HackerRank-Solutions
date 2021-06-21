# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

miu, stdev = map(float, '20 2'.split())  # map(float, input().split())
limit = 19.5 # float(input())
limit1, limit2 = map(float, '20 22'.split())  # map(float, input().split())

def normal_prob(miu, stdev, x):
    return 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))

print( '{:.3f}'.format(normal_prob(miu, stdev, limit)) )
print( '{:.3f}'.format(normal_prob(miu, stdev, limit2) - normal_prob(miu, stdev, limit1)) )
