f=open('a.txt','w')
f.write("This is a line of txt\n")
f.write("This is a second line of txt\n")
for i in range(100):
   f.write(str(i)+","+str(i**2))
f.close()

