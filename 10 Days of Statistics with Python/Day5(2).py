# Enter your code here. Read input from STDIN. Print output to STDOUT
miu_A, miu_B = map(float, input().split())

cost_A = 160 + 40*(miu_A + miu_A**2)
print(round(cost_A, 3))
cost_B = 128 + 40*(miu_B + miu_B**2)
print(round(cost_B, 3))
