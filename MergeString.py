def mergeStrings(string1,string2):
    splitstr1=string1.split()
    splitstr2=string2.split()
    merge=""
    smaller=min(len(splitstr1),len(splitstr2))
    for i in range(smaller):
        merge+=splitstr1[i] + " " + splitstr2[i] + " "
    if len(splitstr1) > len(splitstr2):
        for i in range(smaller,len(splitstr1)):
            merge+=splitstr1[i] + " "
    elif len(splitstr2) > len(splitstr1):
        for i in range(smaller,len(splitstr2)):
            merge+=splitstr2[i] + " "
    return merge

print mergeStrings("hey you buy me this", "what now?")
