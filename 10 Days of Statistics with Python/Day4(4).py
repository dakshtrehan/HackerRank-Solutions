# Enter your code here. Read input from STDIN. Print output to STDOUT
geom = lambda n, p ,q: pow(q, n - 1) * p
a, b = map(int, input().split())
n = int(input())
p = a / b
P = 0
for i in range(1, n + 1):
        P += geom(i, p, 1 - p)
print(round(P, 3))
