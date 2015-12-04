def StripPunc(s):
      new =""
      for x in range(0,len(s)):
          if (s[x]>='a' and s[x]<='z') or (s[x]>='A' and s[x]<='Z') or s[x]==" " or s[x]=="\n":
              new+=s[x]
          else:
              new==""  
      return new.split()
          
print StripPunc('''Hey! listen!
Hey, Hey, Hey!
Listen!
Please: Listen!!!''')

print StripPunc('a.b.c,f:g,K!')
'a.b.c,f:g,K!'.split()
