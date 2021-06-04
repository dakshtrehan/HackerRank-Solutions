# Enter your code here. Read input from STDIN. Print output to STDOUT

size = int(input())
numbers = list(map(int, input().split()))

#mean
print(sum(numbers)/len(numbers))

#median
numbers.sort()
if len(numbers)%2!=0:
    print(numbers[int(len(numbers)/2)])
else:
    print( (numbers[int((len(numbers)-1)/2)] + numbers[int((len(numbers)+1)/2)] )/2)
    
#mode
dict1={}
for i in numbers:
    dict1[i]=0
for i in numbers:
    dict1[i]+=1
    
x=max(dict1.values())
for i in dict1:
    if dict1[i]==x:
        print(i)
        break




    
