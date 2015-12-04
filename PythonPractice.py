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

def near_hundred(n):
    if abs(n - 100) <= 10 or abs(n - 200) <= 10:
        return True
    else:
        return false

def pos_neg(a, b, negative):
    if a < 0 and b > 0 and negative == False:
        return True
    else:
        if a > 0 and b < 0 and negative == False:
            return True
        else:
             if a < 0 and b < 0 and negative == True:
                 return True
            else:
                    return False

def caught_speeding(speed, is_birthday):
    if speed <= 60 and (is_birthday == False or is_birthday == True):
        return 0
    if speed > 60 and speed <= 80 and is_birthday == False:
        return 1
    if speed > 80 and is_birthday == False:
        return 2
    else: return 0

def sorta_sum(a, b):
    if a + b > 10 and a + b < 19:
        return 20
else:
        return a + b

def alarm_clock(day, vacation):
    if day >= 1 and day <= 5 and vacation == False:
        return "7:00"
    if day == 0 or day == 6 and vacation == False:
        return "10:00"
    if day >= 1 and day <= 5 and vacation == True:
        return "10:00"
    if (day == 0 or day == 6) and vacation == True:
        return "off"

def lone_sum(a, b, c):
    if a == b and b == c
    return 0
    if a == b:
        return c
    if b == c:
        return a
    if a == c:
        return b 
    
    
