
def isSameTree(p, q):
    if len(p)!=len(q):
        return None
    else:
        for i in p:
            for j in q:
                if i==j:
                    q=q[1:]
                    break
                else:
                    return None
        return 0
p=[1,2,3]
q=[1,2,3]
if isSameTree(p,q) == None:
    print('not the same')
else:
    print("same")