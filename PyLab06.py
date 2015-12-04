def sumList(L):
    x = 0
    sum = 0
    while x < len(L):
        sum = sum + L[x]
        x = x + 1
    return sum

print sumList([3,4,10])

def makeSentence(L):
    x = 0
    sentence = ""
    while x < len(L):
        sentence = sentence + " " + L[x]
        x = x + 1
    return sentence

print makeSentence( ['The','rain','in','Spain','falls','mainly'])

def makeListOfSquares(n):
    List = []
    x = 1
    while x <= n:
        List.append(x**2)
        x = x + 1
    return List

print makeListOfSquares(5) 

def makeFibList(n):
    List = [0 ,1]
    count = 0
    while count < n-1:
        List.append(List[count] + List[count+ 1])
        count = count + 1
    return List

print makeFibList(5)

def find(part,whole):
    x = 0
    while x < len(whole)-len(part):
        if whole[x:x + len(part)] == part:
            return x
        elif x == len(whole)-len(part) - 1:
            return -1
        else:
            x = x + 1


print find('bc','bcdefga')
print find('abc','bcdefga')
print find('cde','bcdefga')
