results=open('results.txt','w')
values=open('values.txt','r')
operators=open('operators.txt','r')

operlist=operators.readlines()
valuelist=values.readlines()
labels=(valuelist[0].strip('\n')).split(',')

def Operate(op,a,b):
    if op=='+':
        return str(float(A) + float(B))
    elif op=='-':
        return str(float(A) - float(B))
    elif op=='*':
        return str(float(A) * float(B))
    else:
        return str(float(A) / float(B))
    
for i in range(len(operlist)):
    operline=operlist[i]
    valueline=valuelist[i+1]
    A=valueline.split(',')[labels.index(operline.split()[0])]
    B=valueline.split(',')[labels.index(operline.split()[2])]
    op=operline.split()[1]
    results.write(Operate(op,A,B)+"\n")

results.close()
