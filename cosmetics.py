#load library
import matplotlib.pyplot as plt#for plots
import numpy as np #for arrays and lists
import math#needed for pi
#We now obtain the ndarray object of angles between 0 and 2π using the arange() function from the NumPy library.
x=np.arange(0,math.pi*2,0.05)#values for x-axis
sin_y=np.sin(x)#values for y-axis
cos_y=np.cos(x)
#plot that values using plot() fucntion 
#symbols=- , –, -., , . , , , o , ^ , v , < , > , s , + , x , D , d , 1 , 2 , 3 , 4 , h , H , p , | , _
#colors b, g, r, c, m, y, k, w
plt.plot(x,sin_y,'r+')
plt.plot(x,cos_y,'gH')
plt.legend(labels = ('sin', 'cos'), loc = 'lower left') # legend placed at lower right
#set label and title
plt.xlabel("angle")
plt.ylabel("sin-values")
plt.title("Sin-Graph")
#for display other than jupyter 
plt.grid(color='b', ls = '-.', lw = 0.25)
plt.show()

