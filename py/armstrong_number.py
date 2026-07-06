n=int(input())
dummy=n
summ=0
l=len(str(n))
while dummy>0:
    rem=dummy%10
    summ+= rem**l
    dummy=dummy//10
if n==summ:
    print(f'{n} is armstrong')
else:
    print(f'{n} is armstrong')