def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    pos=nums[0]
    k=1
    for i in nums[1:]:
        if pos ==i:
            nums.remove(i)
        else:
            pos=i
            k+=1
    return nums,k

print(removeDuplicates(0,[0,0,1,1,1,2,2,3,3,4]))
