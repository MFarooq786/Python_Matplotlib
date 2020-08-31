#load library
import matplotlib.pyplot as plt#for plots
import numpy as np #for arrays and lists
import math#needed for pi
#We now obtain the ndarray object of angles between 0 and 2π using the arange() function from the NumPy library.
x=np.arange(0,math.pi*2,0.05)#values for x-axis
y=np.sin(x)#values for y-axis
#plot that values using plot() fucntion 
plt.plot(x,y)
#set label and title
plt.xlabel("angle")
plt.ylabel("sin-values")
plt.title("Sin-Graph")
#for display other than jupyter 
plt.show()

