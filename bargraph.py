def makeBar(n):
    x=0
    bar=""
    while x<n:
        bar=bar+"="
        x=x+1
    return bar

def makeBarGraph(L):
    x=0
    graph=""
    while x<len(L):
        graph=graph + str(x) + ":" + makeBar(L[x]) + "\n"
        x=x+1
    return graph

print makeBarGraph([3,0,1,2]) 
print makeBar(4)

def barGraphVertical(L):
    x=0
    graph=""
    while x<len(L):
        graph=graph+str(x)
        x=x+1
    graph=graph+"\n"
    x=0
    y=0
    counter=0
    while x<max(L):
        while y<len(L):
            if counter<L[x]:
                graph=graph+"="
                x=x+1
            else:
                x=x+1
            
