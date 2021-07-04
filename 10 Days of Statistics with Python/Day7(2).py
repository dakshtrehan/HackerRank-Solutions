# Enter your code here. Read input from STDIN. Print output to STDOUT
import functools

n= int(input())
x_lst= list(map(float, input().split()))
y_lst= list(map(float, input().split()))

x_sorted= sorted(x_lst)
y_sorted= sorted(y_lst)

rx=[]
ry=[]

for i,(x,y) in enumerate(zip(x_lst,y_lst)):
    for j,(xs,ys) in enumerate(zip(x_sorted[::-1],y_sorted[::-1])):
        if(x==xs): rx.append(n-j)
        if(y==ys): ry.append(n-j)
        
di=list(map(lambda x,y:x-y, rx,ry))
di_square=list(map(lambda x:x**2, di))
    
sum_di_square= functools.reduce(lambda res,di_square: res + di_square, di_square)

r_xy= 1-((6*sum_di_square)/(n*(n**2-1)))

print(round(r_xy,3))
