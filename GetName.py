#!/usr/bin/python
print "Content-Type: text/html\n"

import cgi
import cgitb
cgitb.enable()

elements = cgi.FieldStorage() 

keys = elements.keys()  
for stuff in keys:
    print "<b>"+str(elements[stuff].value)+"</b>"
