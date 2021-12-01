def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        # rtn='23466644'
        # i=0
        # l=i+1
        # count=1
        # for p in range(n-1):
        #     while l<len(rtn):
        #         if rtn[int(i)]==rtn[int(l)]:
        #             count+=1
        #             l+=1
        #         else:
        #             rtn=str(count)+rtn[int(l)]+rtn
        #             i=l
        #             l=i+1
        #             count=1
        #     rtn=str(count)+rtn[int(l)-1]+rtn[l:]
        #     i=l
        #     l=i+1
        #     count=1
        # return rtn

        count=1
        rtn='1' 
        for a in range(n-1):
            tmp=''
            for i in range(len(rtn)):
                if i==len(rtn)-1:
                    tmp=tmp+str(count)+rtn[i]
                    count=1
                    continue
                if rtn[i]!=rtn[i+1]:
                    tmp=tmp+str(count)+rtn[i]
                    count=1
                else:
                    count+=1
            rtn=tmp
        return rtn

print(countAndSay(0,4))