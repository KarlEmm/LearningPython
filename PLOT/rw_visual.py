import matplotlib.pyplot as plt
from random_walk import RandomWalk

cmap = plt.cm.Blues

# Keep making new wlaks, as long as the program is active.
while True:
  walk = RandomWalk(50_000)
  walk.fill_walk()
  length = walk.num_points
  fig, ax = plt.subplots()
  ax.scatter(walk.x_values, walk.y_values, color=cmap, linewidth=1)
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)
  plt.show()

  keep_running = input("Make another walk? (y/n): ")
  if keep_running == 'n':
    break