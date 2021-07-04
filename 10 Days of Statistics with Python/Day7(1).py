import math as m
n = int(input())
L1 = list(map(float, input().split()))
L2 = list(map(int, input().split()))
mean1 = sum(L1)/n
mean2 = sum(L2)/n
l1 = list()
l2 = list()
l = list()
for i in L1:
    s1 = (i - mean1)**2
    l1.append(s1)
S1 = sum(l1)
std1 = m.sqrt(S1/(n))
for i in L2:
    s2 = (i - mean2)**2
    l2.append(s2)
S2 = sum(l2)
std2 = m.sqrt(S2/(n))
for i in range(n):
        s = (L1[i] - mean1)*(L2[i] - mean2)
        l.append(s)
S = sum(l)
res = S/(n*std1*std2)
print(round(res, 3))
