import matplotlib.pyplot as plt
import numpy as np
a_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
b_grades = [30, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(grades_range,a_grades,color='r')
plt.scatter(grades_range,b_grades,color='b')
plt.title('scatter plot')
plt.xlabel('grade range')
plt.ylabel('obtained score')
plt.legend(labels=('a','b'),loc='upper right')
plt.show()