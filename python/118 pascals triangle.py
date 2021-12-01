# using the powers of 11
# def generate(self, numRows):
#         """
#         :type numRows: int
#         :rtype: List[List[int]]
#         """
#         i=0
#         list_ret=[]
#         while i<(numRows-1):
#             new=[]
#             a=11**i
#             while a>0:
#                 o=a%10
#                 a=a//10
#                 new=[o]+new
#             list_ret.append(new)
#             i+=1
#         return list_ret

def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if not numRows:
            return []
        if numRows==1:
            return [[1]]
        triangle=[[1],[1,1]]
        for i in range(3,numRows+1):
            tmp=[1]
            for l in range(len(triangle[-1])-1):
                l_tmp=triangle[-1][l]+triangle[-1][l+1]
                tmp.append(l_tmp)
            tmp+=[1]
            triangle.append(tmp)
        return triangle

print(generate(0,10))