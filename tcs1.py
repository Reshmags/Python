n=int(input())
l=list(map(int,input().split(' ')))
c=0
max=0
for i in range(n):
    if  l[i]< max:
        c+=1
    else:
        max=l[i]
print(c)
