def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    rtn=''
    words=s.split()
    for i in words:
        rtn=i+' '+rtn
    return rtn[:-1]
print(reverseWords(0,"Alice does not even like bob"))