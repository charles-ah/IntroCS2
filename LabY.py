def numToWords99(i):
    if i == 1:
        return "one "
    if i == 2:
        return "two "
    if i == 3:
        return "three "
    if i == 4:
        return "four "
    if i == 5:
        return "five "
    if i == 6:
        return "six "
    if i == 7:
        return "seven "
    if i == 8:
        return "eight "
    if i == 9:
        return "nine "
    if i == 10:
        return "ten "
    if i == 11:
        return "eleven "
    if i == 12:
        return "twelve "
    if i == 13:
        return "thirteen "
    if i == 14:
        return "fourteen "
    if i == 15:
        return "fifteen "
    if i == 16:
        return "sixteen "
    if i == 17:
        return "seventeen "
    if i == 18:
        return "eighteen "
    if i == 19:
        return "nineteen "
    if i / 10 == 2:
       return "twenty " + numToWords99(i%10)
    if i / 10 == 3:
       return "thirty " + numToWords99(i%10)
    if i / 10 == 4:
       return "fourty " + numToWords99(i%10)
    if i / 10 == 5:
       return "fifty " + numToWords99(i%10)
    if i / 10 == 6:
       return "sixty " + numToWords99(i%10)
    if i / 10 == 7:
       return "seventy " + numToWords99(i%10)
    if i / 10 == 8:
       return "eighty " + numToWords99(i%10)
    if i / 10 == 9:
       return "ninty " + numToWords99(i%10)

def numToWords999(i):
    if i/10 >= 10 and i/10 < 100:
        return numToWords99(i/100) + "hundred " + numToWords99(i%100)

def intToString9999(i):
    if i/100 > 1 and i/100 < 100:
        return numToWords99(i/100) + "hundred " + numToWords99(i%100)
    else:
        return numToWords99(i)
    
    
def numToString(x):
    if x<0:
        return "negative "+numToString(abs(x))
        #this handles negative numbers 
    if x==0:
        return "zero"
        #this is the only time you ever say the word Zero
    if x>0:
        return intToString9999(x) 

print  numToString(56)
print  numToString(78)
print  numToString(49)
print  numToString(13)
print  numToString(345)
print  numToString(9999)
