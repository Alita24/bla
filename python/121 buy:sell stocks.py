def maxProfit(self, prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices:
        return 0
    start=0
    end=len(prices)-1
    diff=0
    for i in prices[1:]:
        
        if i<prices[start]:
            start=prices.index(i)
            end=len(prices)-1
        elif prices[end]<i:
            end=prices.index(i)
        tmp=prices[end]-prices[start]
        if tmp>diff:
            diff=tmp
    return diff

print(maxProfit(0,[0,1,2,8]))
