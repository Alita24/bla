def whole(self, digits,i):
    digits[i-1]+=1
    digits[i]=0
    return digits

def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i=-1
        digits[i]=digits[i]+1
        while digits[i]>9:
            if i==-len(digits):
                digits.insert(0,0)
            whole(0,digits,i)
            i-=1

        return digits
print(plusOne(0,[9,9,9,9,9,9,9,9,9,9,9]))