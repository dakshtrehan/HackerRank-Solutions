# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

miu, stdev = map(float, input().split())
limit1 = float(input())
limit2 = float(input())

def normal_prob(miu, stdev, x):
    return 0.5 + 0.5*math.erf((x-miu)/(stdev * 2**0.5))

print( '%.2f' %((1 - normal_prob(miu, stdev, limit1)) *100) )
print( '%.2f' %((1 - normal_prob(miu, stdev, limit2)) *100) )
print( '%.2f' %(normal_prob(miu, stdev, limit2) *100) )
# note: need to output percentage (not probability)
