f=open("micy.gif","rb")
f2=open("bicy.gif","wb")

for i in f:
    print(i)
    f2.write(i)

f.close()
f2.close()

# with open("example.txt", "w") as file:
#     content = file.read()
#     print(content)

f3=open("example.txt","r",encoding="utf-8")
for i in f3:
    print(i)