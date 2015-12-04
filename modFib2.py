#!/usr/bin/python
print "content-type: text/html\n"
import cgi,cgitb
cgitb.enable()

def G(n):
    num = 0
    if n == 0:
        return 0

    if n == 1:
        return 1


    num  = ( G(n-1) + G(n-2) )**2

    return num
    
def W(n):

    num = 0
    if n == 0:
        return 0

    if n == 1:
        return 1


    num  = W(n-1)**2 + W(n-2)**2;

    return num;
    

def sumDig(n):

    sum = 0
    i=0
    while i < len(n):
        sum += int(n[i])

    return sum

print G(30)
print sumDig(str(G(30) - W(30)))
