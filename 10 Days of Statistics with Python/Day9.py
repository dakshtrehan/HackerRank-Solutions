# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy as np

m, n = map(int, input().split())
xy = [list(map(float, input().split())) for _ in range(n)]
y = np.array([i.pop() for i in xy])
X = np.array(xy)

b = np.ones(n)
X = np.c_[b, X]
B = np.linalg.inv(X.T.dot(X)).dot(X.T).dot(y)

q = int(input())
for _ in range(q):
    k = np.array(input().split(), float)
    print(B.dot(np.insert(k, 0, 1)))
