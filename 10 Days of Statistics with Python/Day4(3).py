def g(trial,p):
    return round(((1-p)**(trial-1))*(p),3)

r,d = list(map(float, input().split(" ")))
p = r/d
n = list(map(float, input()))[0]

print(g(n,p))
