from turtle import *
sc=Screen()
sc.setup(800,400)
l=['red','green','blue','orange','yellow']
for i in range(100):
    pencolor(l[i%5])
    #pensize(i%10)
    fd(i*10)
    left(145)

done()