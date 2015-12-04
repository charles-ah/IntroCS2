#!/usr/bin/python
print "Content-type: text/html\n"


import cgi
import cgitb
cgitb.enable()

mathdata=cgi.FieldStorage()

def Operate(A,B,op,dataType):
    if dataType=='Decimal':
        if op=='+':
            return float(A)+float(B)
        elif op=='-':
            return float(A)-float(B)
        elif op=='*':
            return float(A)*float(B)
        elif op=='/':
            return float(A)/float(B)
    elif dataType=='Integer':
        if op=='+':
            return int(A)+int(B)
        elif op=='-':
            return int(A)-int(B)
        elif op=='*':
            return int(A)*int(B)
        elif op=='/':
            return int(A)/int(B)

if mathdata['font'].value=='Bold':
    print "<b>" + str(Operate(mathdata['A'].value,mathdata['B'].value,mathdata['operator'].value,mathdata['dataType'].value)) + "</b>"
elif mathdata['font'].value=='Italic':
    print "<i>" + str(Operate(mathdata['A'].value,mathdata['B'].value,mathdata['operator'].value,mathdata['dataType'].value)) + "</i>"


