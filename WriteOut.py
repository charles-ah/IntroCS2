f=open('out.txt','w')
x=open('in.txt','r')

def Operate(line):
    listeq=line.split()
    if listeq[1]=='+':
        return str(float(listeq[0]) + float(listeq[2]))
    elif listeq[1]=='-':
        return str(float(listeq[0]) - float(listeq[2]))
    elif listeq[1]=='*':
        return str(float(listeq[0]) * float(listeq[2]))
    else:
        return str(float(listeq[0]) / float(listeq[2]))

    

for line in x.readlines():
    f.write(line.strip('\n') + " = " + Operate(line) + "\n")

