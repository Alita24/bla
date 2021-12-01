
# pesel verification

num=input('please provide with pesel number: ')


def checkPesel(num):
    if len(num)!=11:
        return False
    else:
        num=str(num)
        last=num[-1]
        num=num[:-1]
        multi=[1,3,7,9]
        o=0
        z=0
        for i in num:
            z=z+int(i)*multi[o]
            o+=1
            o=o%4
        z=z%10
        if z!=0:
            z=10-z
        if z==int(last):
            return True
        else:
            return False

print(checkPesel(num))