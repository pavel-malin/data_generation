import matplotlib.pyplot as plt

from random_walk import RandomWalk

# New walks are built as long as the program remains active.
while True:
    # Construction of random walk and drawing points on the chart. 
    rw = RandomWalk() # 50000
    rw.fill_walk()

    # Viewport Size Name
    # plt.figure(figsize=(10, 6))
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    # plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
    #            edgecolors='none', s=1)
    
    # Select the first and last points.
    # plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    # plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none',
    #            s=100)
    plt.plot(rw.x_values, rw.y_values, linewidth=14)
    # Removing axles.
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make anther walk? (y/n): ")
    if keep_running == 'n':
        break

