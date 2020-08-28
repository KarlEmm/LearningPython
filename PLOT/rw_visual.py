import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Using matplotlib, trace the path the program randomly takes through the
# imported RandomWalk class.

# Keep making new walk, as long as the program is active.
while True:
  size = 50_000
  walk = RandomWalk(size)
  walk.fill_walk()
  length = walk.num_points
  fig, ax = plt.subplots()
  ax.scatter(walk.x_values, walk.y_values, c=range(size), cmap=plt.cm.coolwarm, s=1)
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break