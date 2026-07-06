l1=eval(input())#[1,6,2,9,2,9]
l2=[]
for ele in l1:
    if ele not in l2:
        l2.append(ele)
print(l2)#[1, 6, 2, 9]