import matplotlib.pyplot as plt
import numpy as np
plt.axis('equal')
langs = ['C', 'C++', 'Java', 'Python', 'PHP']
students = [23,17,35,29,12]
plt.pie(students,labels=langs,autopct='%1.2f%%')
plt.show()