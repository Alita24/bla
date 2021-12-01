#exceedes the time limit

# def rotate(self, nums, k):
#     while k>0:
#         nums.insert(0,nums.pop())
#         k-=1
#     return nums

# also time exceeded

# def rotate(self, nums, k):
#     for i in range(k):
#         tmp=nums.pop()
#         nums.insert(0,tmp)
#     return nums

def rotate(self, nums, k):
    nums[:]=nums[(len(nums)-k)%(len(nums)):]+nums[:(len(nums)-k)%(len(nums))]
    return nums
print(rotate(0,[1],0))