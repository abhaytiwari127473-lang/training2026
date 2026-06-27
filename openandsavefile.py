f=open("ifelse.py","r")
f1=open("myfile.py","w")
#print(f)
for i in f:
    print(i,end='')
    f1.write(i)