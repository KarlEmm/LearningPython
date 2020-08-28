import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
size = 3000 
x_values = [x for x in range(size)]
y_values = [x**3 for x in range(size)]

plt.style.use('seaborn')
ax.set(xlabel='x', ylabel='y', title='Cube')
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.hsv)

plt.show()

