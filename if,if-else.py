#if:


#wap to print the given number if it is greater than 100
n=int(input())
if n>100:
    print(n)

#wap to print the given string if it has more than 5 characters
s=input()
if len(s)>5:
    print(s)


#if-else:


# wap to print the given number is even or odd
n=int(input())
if n%2==0:
    print(f'{n} is even')
else:
    print(f'{n} is odd')

    
# wap to print the maximum number among given two numbers
a=int(input())
b=int(input())
if a>b:
    print(f'{a} is max')
else:
    print(f'{b} is max')

#wap to check given string is palindrome or not
s=input()
if s== s[::-1]:
    print('s is palindrome')
else:
    print('s is not a palindrome')

    
#wap to check given strings are anagrams or not
a=input()
b=input()
if sorted[a]==sorted[b]:
    print('a and b are anagrams')
else:
    print('a and b are not anagrams')


#wap to check the given year is leap year or not
year=int(input())
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not a leap year')



