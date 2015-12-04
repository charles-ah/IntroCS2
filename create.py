#!/usr/bin/python
import cgi,cgitb,os,random,md5
cgitb.enable()

def header():
    return """content-type: text/html

<!DOCTYPE HTML>
<html>
<head>
<title>Create account</title>
</head>
<body>
"""

def footer():
    return """</body>
</html>"""

def md5Pass(password):
    m = md5.new()
    m.update(password)
    return m.hexdigest()

def checkIfNameExists(user):
    text = open('users.txt').read().split("\n")
    for line in text:
        if line.split(",")[0]==user:
            return True
    return False

def valid(s):
    for c in s:
        if not (c >= 'a' and c <= 'z' or c >= 'A' and c <= 'Z' or c >= '0' and c <= '9'):
            return False
    return True

def createAccount(form):
    result = "attempting to create an account...<br>"
    if "user" in form and "pass" in form and "pass2" in form:
        user = form.getvalue("user")
        password = form.getvalue("pass")
        password2 = form.getvalue("pass2")
        if checkIfNameExists(user):
            result += "user exists: "+ user +"<br>"
        elif password != password2:
            result += "passwords do not match!<br>"
        elif not valid(user):
            result += "username contains invalid characters<br>"
        else:
            result += "account "+user+' created! login here: <a href="login.html">login page</a><br>'
            f = open('users.txt','a')
            password = md5Pass(password+user)
            f.write(user+","+password+"\n")
            f.close()
    else:
        result+="<h1>Invalid form submission, please fill in all fields</h1>"
    return result


    


def notFilledIn():
    return '''You need to create an account using the form found <a href="create.html">here</a>\n'''

def main():
    form = cgi.FieldStorage()
    body = ""
    if len(form)==0:
        body += notFilledIn()
    else:
        body += createAccount(form)
    print header() + body + footer()

main()


