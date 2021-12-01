def generate(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[List[int]]
        """
        
        if not rowIndex:
            return [1]
        tmp=[1]
        for i in range(1,rowIndex+1):
            for l in range(1,len(tmp)):
                tmp[l-1]+=tmp[l]
            tmp.insert(0,1)
        return tmp
        

print(generate(0,3))