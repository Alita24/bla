def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    rtn=''
    for i in s:
        if 65<=ord(i)<=90 or 97<=ord(i)<=122 or 48<=ord(i)<=57:
            rtn+=i
    rtn=rtn.lower()
    # solution1
    # half=len(rtn)//2
    # for l in range(half):
    #     if rtn[l]==rtn[-l-1]:
    #         continue
    #     else:
    #         return False
    # return True

    # solution2
    # if rtn==rtn[::-1]:
    #     return True
    # else: 
    #     return False

    # solution3
    # return rtn==rtn[::-1]
print(isPalindrome(0,'race a car'))

    
