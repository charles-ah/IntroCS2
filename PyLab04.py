#Charles Zhang
#pd 2
#PyLab04

def rot13char(c):
    if (c >= 'A' and c <= 'M') or (c >= 'a' and c <= 'm'):
            return chr(ord(c) + 13)
    elif (c >= 'N' and c <= 'Z') or (c >= 'n' and c <= 'z'):
            return chr(ord(c) - 13)
    else:
        return c

print rot13char('a')
print rot13char('A')
print rot13char('N')
print rot13char('-')

def rot13(s):
    x = 0
    rot = ""
    while x < len(s):
        rot = rot + rot13char(s[x])
        x = x + 1
    return rot

print rot13('CLERK')
print rot13('she-HEY!')

def rotXchar(c,x):
    if (c >= 'A' and c <= 'M') or (c >= 'a' and c <= 'm'):
            return chr(ord(c)% + x)
    elif (c >= 'N' and c <= 'Z') or (c >= 'n' and c <= 'z'):
            return chr(ord(c) + x - 26)
    else:
        return c
    

def rotX(s,x):
    x = 0
    rot = ""
    while x < len(s):
        rot = rot + rotXchar(s[x],x)
        x = x + 1
    return rot

print rotX('Gjnf oevyyvt naq gur fyvgul gbirf, qvq tler naq tvzoyr va gur jnor.',1)
print rotX('what',13)
