import matplotlib.pyplot as plt
import numpy as np
entries = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
plt.hist(entries,bins=[0,25,50,75,100])
plt.xticks([0,25,50,75,100])
plt.title("histogram of results")
plt.xlabel("makrs")
plt.ylabel("no.of students")
plt.show()