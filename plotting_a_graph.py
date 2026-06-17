import matplotlib.pyplot as mp
#from matplotlib.pyplot import *
#from  math import*
import math as m
day=[1,2,3,4,5,6,7]
maxtemp=[m.sqrt(41),m.sqrt(39),m.sqrt(42),m.sqrt(26),m.sqrt(18),m.sqrt(42),m.sqrt(38)]
mintemp=[12,18,5,25,16,41,12]
mp.title("Weather Graph")
mp.xlabel("Day")
mp.ylabel("Temperature")
mp.plot(day,mintemp,color="blue",label="min")
mp.plot(day,maxtemp,color="red",linewidth=5,linestyle=':',label="max")
mp.savefig("g.jpg")
mp.legend(loc="best",shadow=True,fontsize="large")
mp.grid()
mp.show()
mp.close()