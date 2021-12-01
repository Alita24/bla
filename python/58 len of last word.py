def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=s.split()
        if not l:
            return 0
        return len(l[-1])
print(lengthOfLastWord(0,'a '))