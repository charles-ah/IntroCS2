#!/usr/bin/python
print "Content-Type: text/html\n"
print ""

print "<!DOCTYPE html><html> <body>"
def readFileIntoLists(filename):
        lines = open(filename).read().split("\n")
        for line in lines:
                line.split(",")
        return lines


def getHeader(L):
        return L[0]

def getData(L):
        while L[-1] == ['']:
                L=L[:-1]
        return L[1:]


data1 = readFileIntoLists("pokemon.csv")

pokeGeneralH =  getHeader(data1)
pokeGeneral = getData(data1)#[:10]

data2 = readFileIntoLists("pokemon_stats.csv")
pokeStatsH = getHeader(data2)
pokeStats = getData(data2)


data3 = readFileIntoLists("stats.csv")
statsH = getHeader(data3)
stats = getData(data3)

#uses _stats
def getStatName(Id):
        if Id < 1 or Id > 8:
                print "invalid stat id:"+str(Id)
                return "invalid!"
        Id = str(Id)
        Id = str(Id)
        for line in stats:
                if line[0]==Id:
                        return line[2]
        print "invalid value, reached end of getStatName"
        return "invalid value, reached end of getStatName"
                
#uses _stats
def getStatID(s):
        statNames = [ a[2] for a in stats]
        statNames = ["error"]+statNames
        if not s.lower() in statNames:
                return -1
        return statNames.index(s.lower())
print "hello</html>"

