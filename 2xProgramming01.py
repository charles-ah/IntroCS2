def toUpper(s):
    x = 0
    new = ""
    while x < len(s):
        if s[x] >= 'a' and s[x] <= 'z' :
             new = new + chr(ord(s[x]) - 32)
        else:
            new = new + s[x]
        x = x + 1
    return new

print toUpper('Bing! Wah?')

def stringReverse(s):
    x = len(s) -1
    new = ""
    while x >= 0:
        new = new + s[x]
        x=x-1
    return new

print stringReverse('hello')

def countCharInString(s,c):
    x=0
    count=0
    while x < len(s):
        if s[x] == c:
            count = count + 1
        x=x+1
    return count

print countCharInString('Bobby Brown','b')

def makeBoxOfNumbers(rows,cols):
    x=1
    countRows=1
    countCols=1
    new=""
    while countRows <= rows:
        while countCols <=cols:
            new = new + str(x%10)
            countCols=countCols + 1
            x=x+1
        new =new + "\n"
        countRows = countRows + 1
        countCols = 1

    return new
print makeBoxOfNumbers(3,6)

def findInString(part,target):
    x = 0
    while x < len(target)-len(part):
        if target[x:x+len(part)] == part:
            return x
        else:
            x=x+1
print findInString('by','Abbye by bye')

def removeFromString(s,c):
    x=0
    new=""
    while x < len(s):
        if s[x] == c:
            x=x+1
            new = new + s[x]
        else:
            new = new + s[x]
            x=x+1
            
    return new
print removeFromString('Bloop pow woot', 'o')

