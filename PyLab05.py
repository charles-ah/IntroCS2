def bondify(name):
    x = 0
    while name[x] != " ":
        x = x + 1
    return name[x + 1:] +", " + name


print bondify("Xiao-Xiao Zhou")
print bondify("James Bond")

def PigLatin(word):
    x = 0
    if word[0] == 'a' or word[0] == 'e' or word[0] == 'i' or word[0] == 'o' or word[0] == 'u':
        return word + "ay"
    else:
        while x < len(word):
            if word[x] == 'a' or word[x] == 'e' or word[x] == 'i' or word[x] == 'o' or word[x] == 'u':
                return word[x:] + word[:x] +"ay"
            else: x = x + 1

print PigLatin('egg')
print PigLatin('somalia')
print PigLatin('cheese')
    
