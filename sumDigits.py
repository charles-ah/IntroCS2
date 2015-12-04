def sumDigits(n):
    sum = 0
    while n >= 1:
        sum = sum + n%10
        n = n/10
    return sum

print sumDigits(591)

def sumDigitsrec(n):
    if n >= 1:
        return n%10 + sumDigitsrec(n/10)
    else:
        return 0

print sumDigitsrec(134)
