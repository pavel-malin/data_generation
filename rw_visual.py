import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Construction of random walk and drawing points on the chart. 
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
