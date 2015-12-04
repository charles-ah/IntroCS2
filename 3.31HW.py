#1

def mean(L):
    total=0
    for x in L:
        total+=x
    return total/len(L)

print mean([1,2,3])

#2

def maxInt(L):
    newMax=0
    for x in L:
        if newMax>x:
            newMax=newMax
        else:
            newMax=x
    return newMax

print maxInt([1,2,4,2])

#3



