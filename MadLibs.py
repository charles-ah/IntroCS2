#!/usr/bin/python
print "Content-Type: text/html\r\n"

import random

def madlibs(storyString, nounList, verbList, adjectiveList):
    new=""
    x=0
    while x<len(storyString):
        if storyString[x:x+4]=="NOUN":
            new+="<b>" + nounList[random.randint(0,len(nounList)-1)] + "</b>"
            x+=4
        else:
            new+=storyString[x]
            x+=1
    x=0
    new1=""
    while x<len(new):
        if new[x:x+4]=="VERB":
            new1+="<b>" + verbList[random.randint(0,len(verbList)-1)] + "</b>"
            x+=4
        else:
            new1+=new[x]
            x+=1
    x=0
    new2=""
    while x<len(new1):
        if new1[x:x+9]=="ADJECTIVE":
            new2+="<b>" + adjectiveList[random.randint(0,len(adjectiveList)-1)] + "</b>"
            x+=9
        else:
            new2+=new1[x]
            x+=1
    return "<html>\n<head><title>MadLibs</title><head>\n<body>\n <h1> Lincoln's Stuyvesant Address </h1>\n" + new2 + "\n</body>"
    
            
 
text='''Four score and seven years ago our fathers VERBed forth on this NOUN, a new NOUN, conceived in NOUN, and VERB to the proposition that all NOUNs are created equal.

Now we are VERBing in a ADJECTIVE NOUN war, testing whether that NOUN, or any NOUN so conceived and so VERB, can long endure. We are met on a ADJECTIVE NOUN of that war.

We have come to dedicate a portion of that NOUN, as a ADJECTIVE resting place for those who here gave their lives that that nation might live. It is altogether ADJECTIVE and proper that we should do this.

But, in a ADJECTIVE sense, we can not VERB -- we can not VERB -- we can not hallow -- this NOUN. The brave NOUN, VERBing and dead, who VERBed here, have consecrated it, far above our ADJECTIVE power to add or detract.

The world will little note, nor long VERB what we say here, but it can never forget what they did here. It is for us the NOUN, rather, to be dedicated here to the unfinished work which they who VERBed here have thus far so nobly
advanced.

It is rather for us to be here dedicated to the great task VERBing before us -- that from these honored NOUNs we take ADJECTIVE devotion to that cause for which they gave the last ADJECTIVE measure of devotion -- that we here ADJECTIVE resolve that

these NOUN shall not have VERBed in vain -- that this nation, under NOUN, shall have a ADJECTIVE birth of NOUNs -- and that government of the NOUN, by the NOUN, for the NOUN, shall not VERB from the earth.'''

nouns=['Stuyvesant student','New York','Mr. Moran','Mr. Brown Mykolyk','Mr. K','7th to 9th floor esclators','bathrooms','CS Dojo','phones','11th floor pool','locker rooms','halal cart','Ferrys','stress','textbooks','Netlogo','homework']
verbs=['run','spin','talk','hit','jig','shave','take','break','code','calculated','partially intergrated','differentiate','rave']
adjectives=['silent','big','small','hairy','rich','amazing','outrageous','preposterous','broken','late']

print madlibs(text, nouns, verbs, adjectives)
