
def addBinary(self, a, b):
    """
    :type a: str
    :type b: str
    :rtype: str
    """
    rtn=''
    sum=int(a)+int(b)
    rest=0
    if sum==0:
        return '0'
    while sum>0:
        if (sum%10)+rest>=2:
            rtn=str(((sum%10)+rest)%2)+rtn
            rest=1
        else:
            rtn=str(((sum%10)+rest)%2)+rtn
            rest=0
        sum//=10
    if rest==1:
        rtn='1'+rtn
    return rtn
print(addBinary(0,'111111','1'))