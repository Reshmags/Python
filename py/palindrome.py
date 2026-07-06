

#palindrome string
s=input()
if s== s[::-1]:
    print('s is palindrome')
else:
    print('s is not a palindrome')


#palindrome no(while loop)
n=int(input())
dummy=n
rev=0
while dummy>0:
    rem=dummy%10
    rev= rev*10+rem
    dummy=dummy//10
if n==rev:
    print(f'{n} is palindrome')
else:
    print(f'{n} is palindrome')