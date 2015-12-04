#! /usr/bin/python
print "Content-Type: text/html \n"
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
    rowCount=0
    colCount=0
    
    while rowCount<max(L):
        while colCount<len(L):
            if rowCount<L[colCount]:
                graph=graph+"="
                colCount=colCount+1
            else:
                graph=graph+" "
                colCount=colCount+1
        graph=graph+"\n"
        rowCount=rowCount+1
        colCount=0
    return graph

#print makeGraph([3,0,1,2])

print barGraphVertical([3,4,1,5])
            
