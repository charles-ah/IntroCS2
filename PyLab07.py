def matching(L,M):
    x=0
    counter = 0
    while x<min(len(L), len(M)):
        if L[x] == M[x]:
            counter = counter + 1
            x=x+1
        else:
            x=x+1
    return counter

print matching([1,2,3],[2,3,4]) 

print matching([1,2,3],[2,2,3]) 

print matching([4,1,9,2,3],[2,1,9,2,3,3,3,3]) 

def stringToList(s):
    x=0
    L=[]
    while x<len(s):
        L=L+[s[x]]
        x=x+1
    return L

print stringToList("Hoooot")

def noDupeMatch(L,M):
    x=0
    counter = 0
    if len(L) < len(M):
        while x<len(L):
            
            if str(M).find(str(L[x])) != -1 and L.count(L[x]) == 1:
                counter = counter + 1
                x=x+1
            else:
                x=x+1
    else:
         while x<len(M):

            if str(L).find(str(M[x])) != -1 and M.count(M[x]) == 1:
                counter = counter + 1
                x=x+1
            else:
                x=x+1
    return counter

print noDupeMatch( [3,3,3] , [3,3,3,3,3] )
print noDupeMatch( [5,6,2,8] , [8,6,5,4,2,5,8] ) 
print noDupeMatch( [1,2,3] , [3,3,3,4,5] )                 
            
    
