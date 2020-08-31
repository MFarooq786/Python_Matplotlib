#load library
import matplotlib.pyplot as plt#for plots
import numpy as np #for arrays and lists
import math#needed for pi
#We now obtain the ndarray object of angles between 0 and 2π using the arange() function from the NumPy library.
x=np.arange(1,10)#values for x-axis
expo=np.exp(x)#values for y-axis
#sq=x**2
#plot that values using plot() fucntion 
#symbols=- , –, -., , . , , , o , ^ , v , < , > , s , + , x , D , d , 1 , 2 , 3 , 4 , h , H , p , | , _
#colors b, g, r, c, m, y, k, w
plt.plot(x,expo,'r-')
#plt.plot(x,sq,'g-')
#plt.yscale("log")
plt.xlim(0,10)
plt.ylim(0,10000)
plt.legend(labels = ('exponential'), loc = 'upper left') # legend placed at lower right
#set label and title
plt.xlabel("angle")
plt.ylabel("sin-values")
plt.title("Sin-Graph")
#for display other than jupyter 
plt.grid(color='b', ls = '-.', lw = 0.25)
plt.show()

