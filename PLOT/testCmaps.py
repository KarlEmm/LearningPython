import matplotlib.pyplot as plt

array = [x for x in range(20)]

fig, ax = plt.subplots()
ax.scatter(array, array, c=array, cmap=plt.cm.coolwarm)
plt.show()