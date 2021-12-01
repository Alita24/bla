def removeElement(self, nums, val):
    """
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    if not nums:
        return 0
    k=0
    le=len(nums)
    for i in range(le):
        if nums[i] ==val:
            k+=1
    for i in range(k):
        nums.remove(val)
            
    return le-k,nums
print(removeElement(0,[0, 1, 2,2, 3, 0, 4,2],2))
