# wap to find  how many elements are present in given string
s=input()
c=0
for ele in s:
    c+=1
    print(c)
#or
s=input()
print(len(s))


# wap to find  how many digits are present in given string
s=input()
c=0
for ele in s:
    if ele.isdigit():
        c+=1
print(c)

# wap to find  how many integers are present in given string
s=input()
c=0
for ele in s:
    if ele.isdigit() and type(ele)==int:
        c+=1
print(c)

# wap to find  sum of digits are present in given string
s=input()
su=0
for ele in s:
    if ele.isdigit():
        su+=int(ele)
print(su)

# wap to find  sum of integers are present in given string
s=input()
su=0
for ele in s:
    if ele.isdigit() and type(ele)==int:
        su+=ele
print(su)

# wap to find  sum of even digits present in given string
s=input()
su=0
for ele in s:
    if ele.isdigit() and int(ele)%2==0:
        su+=int(ele)
print(su)

# wap to find  sum of odd digits present in given string
s=input()
su=0
for ele in s:
    if ele.isdigit() and int(ele)%2!=0:
        su+=int(ele)
print(su)

# wap to find  how many special characters are present in given string
s=input()
c=0
for ele in s:
    if ele.isalnum()==False:
        c+=1
print(c)

# wap to find  how many special characters, alphabets, digits are present in given string

s=input()
al=0
sp=0
di=0
for ele in s:
    if ele.isalpha():
        ap+=1
    elif ele.isdigit():
        di+=1
    else:
        sp+=1
print('alphabets:', al)
print('digits:', di)
print('special char:', sp)

