import string

def StoryNoPuncs(s):
    list1=s.split()
    for i in range(len(list1)):
        list1[i]=list1[i].strip(string.punctuation)
        list1[i]=list1[i].lower()
    return s.split()

f=open('Oz.txt','r')
#print StoryNoPuncs(f.read())

def WordTally(L):
    countList=[]
    for x in range(len(L)):
        countList+=[L.count(L[x])]
    for x in range(len(L)):
        print L[x] + ":" + str(countList[x])


WordTally(StoryNoPuncs(f.read()))    
