#!/usr/bin/python
print "Content-type: text/html\n"

print "<!DOCTYPE html> <html> <body>"
def readFileIntoLists(filename):
        lines = (open(filename).read()).split("\n")
        for i in range(len(lines)):
                       lines[i]=lines[i].split(',')
        return lines


def getHeader(L):
        return L[0]

def getData(L):
        while L[-1] == ['']:
                L=L[:-1]
        return L[1:]


pokeGeneralH =  getHeader(readFileIntoLists("pokemon.csv"))
pokeGeneral = getData(readFileIntoLists("pokemon.csv"))
print "hello"
pokeStatsH = getHeader(readFileIntoLists("pokemon_stats.csv"))

pokeStats = getData(readFileIntoLists("pokemon_stats.csv"))


statsH = getHeader(readFileIntoLists("stats.csv"))
stats = getData(readFileIntoLists("stats.csv"))


def getOtherAttributes(pokemon_ID):
    AttributesList=[]
    for i in range(3):
        pokeAttributes=pokeStats[pokemon_ID*6+i]
        AttributesList.append(pokeAttributes[2])
    AttributesList.append(pokeStats[pokemon_ID*6+5][2])
    return AttributesList

def makeSinglePokeList(pokemon_ID):
    Pokelist=[pokemon_ID+1,pokeGeneral[pokemon_ID][1]]
    for i in range(3,5):
        Pokelist.append(pokeGeneral[pokemon_ID][i])
    return Pokelist + getOtherAttributes(pokemon_ID)
   
def makePokeTable():
   tablestr="<table><tr><td>ID</td><td>NAME</td><td>Height</td><td>Weight</td><td>HP</td><td>Attack</td><td>Defense</td><td>Speed</td></tr>"
   for i in range(0,100):
        tablestr+="\n<tr>"
        for stat in makeSinglePokeList(i):
            tablestr+="\n<td>" + str(stat) + "</td>"
        tablestr+="\n</tr>"
   return tablestr + "\n</table>\n</body></html>"    

print makePokeTable()
