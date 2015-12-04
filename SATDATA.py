<<<<<<< HEAD
#! /usr/bin/python
print "content-type: text/html\n
=======
#!/usr/bin/python
print "Content-Type: text/html\r\n"
import cgitb
cgitb.enable()




print "<html>\n<head><title>SAT DATA</title></head>\n<body>\n<table border='1'>"

def table(text):
    tablestr=""
    textlines=text.readlines()
    for line in textlines:
        tablestr+="\n<tr>"
        for word in line.split(','):
            tablestr+="\n<td>" + word + "</td>"
        tablestr+="\n</tr>"
    return tablestr + "\n</table>\n</body>"      
       
data=open('scores.csv','r')
dataread=data.read()
print table(dataread)

    
>>>>>>> ba53e43e3c835520e76163908c81fff742ad0491
