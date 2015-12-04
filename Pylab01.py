#Charles Zhang
#pd 2
#PyLab01

import math

#3.1
def triangleArea(base,height):
    return base * height / 2

#print triangleArea(5,10)

#3.2
def distance(x1,y1,x2,y2):
    return math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 )

#print distance(0,0,3,4)

#3.3

def disc(a,b,c):
    return b**2 - 4*a*c

#print disc(2,3,4)
#print disc(1,2,1)

#3.4

def gradePicker(score):
    if score >= 90:
        return "A"
    elif score >= 80 and score <= 89:
        return "B"
    elif score >= 70 and score <= 79:
        return "C"
    elif score >= 65 and score <= 69:
        return "D"
    else:
        return "F"

#print gradePicker(5)
#print gradePicker(92)

#3.5

def closestPoints(ax,ay,bx,by,cx,cy):
    if distance(ax,ay,bx,by) == distance(bx,by,cx,cy) == distance(ax,ay,cx,cy):
        return 0
    if distance(ax,ay,bx,by) < distance(bx,by,cx,cy) and distance(ax,ay,bx,by) < distance(ax,ay,cx,cy):
        return 1
    if distance(ax,ay,cx,cy) < distance(bx,by,cx,cy) and distance(ax,ay,cx,cy) < distance(bx,by,cx,cy):
        return 2
    if distance(bx,by,cx,cy) < distance(ax,ay,bx,by) and distance(bx,by,cx,cy) < distance(ax,ay,cx,cy):
        return 3
    
#print closestPoints(0,0,1,1,0.1,0.1)
#print closestPoints(-1,0,0,1,1,0) 

#3.6

def numRoots(a,b,c):
    if disc(a,b,c) < 0:
        return 0
    if disc(a,b,c) == 0:
        return 1
    if disc(a,b,c) > 0:
        return 2

#print numRoots(1,4,4)
#print numRoots(1,4,3)
#print numRoots(1,2,4)
#print numRoots(1,6,9)

#3.7

def quadsolvePlus(a,b,c):
        return (-b + math.sqrt(disc(a,b,c))) / 2

#print quadsolvePlus(1,4,4)
#print quadsolvePlus(1,6,9)
#print quadsolvePlus(1,4,3)


#3.8

def quadsolve(a,b,c,sign):
    if sign > 0:
        return quadsolvePlus(a,b,c)
    else:
        return (-b - math.sqrt(disc(a,b,c))) / 2

#print quadsolve(1,4,4,-1)
#print quadsolve(1,6,9,-1)
#print quadsolve(1,4,3,-1)
#print quadsolve(1,4,3,1)

