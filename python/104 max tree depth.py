import math
def maxDepth(root):
    if not root:
        return 0
    return int(1 + math.log(len(root),2))

p=[]
print(maxDepth(p))
