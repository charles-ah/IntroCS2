def sleep_in(weekday, vacation):
    return not weekday or vacation

print sleep_in(True, False)


def monkey_trouble(a_smile, b_smile):
    if a_smile==b_smile:
        return True
    else:
        return False

print monkey_trouble(True, True) 
print monkey_trouble(False, False)
print monkey_trouble(True, False) 

def sum_double(a, b):
    if a==b:
        return 4*a
    else:
        return a + b

def diff21(n):
    if n > 21:
        return 2*abs(n - 21)
    else:
        return abs(n - 21)

def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking == True :
        return True
    else:
        return False


def makes10(a, b):
    if a == 10 or b == 10 or (a + b) == 10:
        return True
    else:
        return False

    
