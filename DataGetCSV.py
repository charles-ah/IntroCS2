text=(open('data.csv','r')).read()
#print text
def getHeader(text):
    textlines=text.split('\n')
    return textlines[0].split(',')

#print getHeader(text)

def getIntData(text):
    textlines=text.split('\n')
    list=[]
    for datalines in textlines[1:-1]:
         list.append(datalines.split(','))
    for line in list:
        for i in range(len(line)):
            line[i]=int(line[i])
    return list
   
print getIntData(text)

headerList = getHeader(text)
dataList = getIntData(text)

for dataline in dataList:
    sum=0
    for x in dataline:
        sum+=float(x)
    print str(sum)


def calcColumnSum(header,data,colname):
    sum=0
    for datalines in dataList:
        sum += float(datalines[headerList.index(colname)])
    return sum

print calcColumnSum(headerList,dataList,"m")
print "+".join(['1','2'])
