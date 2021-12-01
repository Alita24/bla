import math

a=int(input("please declare side one "))
b=int(input("please declare side two "))
c=int(input("please declare side three "))
s=(a+b+c)/2
f=s*(s-a)
f=f*(s-b)
f=f*(s-c)
if f<=0:
    print("are you sure these are the right measurements?")


else :
    g=math.sqrt(f)
    print("the area of this triangle is",g)

