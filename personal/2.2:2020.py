
l=int(input("the number:"))
# l=2374
output=''
while  l>0:
    k=l%10
    l=l//10
    s=0
    while s<4:
        output=str(k%2) + output
        k=k//2
        s+=1
    
print(output)
