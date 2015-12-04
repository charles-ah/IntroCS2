#1 /usr/bin/python
print "content-type:text/html\n"

#1

def startPage(title):
    return "<html>\n<head><title>" + title + "</title></head>\n<body>"

#print startPage("Made-up Page")

#2a

def makeRows(numCols):
    x = 1
    tag = ""
    while x <= numCols:
        tag = tag + "<td>" + str(numCols) + "</td>"
        x = x + 1

    return "\t <tr>" + tag + "</tr>"

#print makeRows(4)

#2b

def makeRow(numCols, startingvalue):
    x = 1
    tag = ""
    while x <= numCols:
        tag = tag + "\n <td>" + str(startingvalue) + "</td>\n"
        x = x + 1
        startingvalue = startingvalue + 1

    return "<tr>" + tag + "</tr>"

#print makeRows(4,99)

#3a

def makeTable(Rows,Cols):
    n = 0
    tables = ""
    while n < Rows:
       tables = tables + "\n" + makeRows(Cols) + "\n"
       n = n + 1

    return "<table> \n" +  tables + "\n </tables>"

#print makeTable(3,4)

#3b

def makeTable(Rows,Cols,startingvalue):
    n = 0
    tables = ""
    while n < Rows:
       tables = tables + "\n" + makeRow(Cols,startingvalue) + "\n"
       n = n + 1
       startingvalue = startingvalue + Cols

    return "<table border= '2' > \n" +  tables + "\n </table>"

#print makeTable(2,4,11)

#4

def makePage():
    return startPage("Blah") + "\n" + makeTable(14,16,32) + "\n </body>"

print makePage()
    

