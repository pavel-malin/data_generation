import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues,
            edgecolors='black', s=50)

# Assigning a chart title and axis labels.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Values", fontsize=14)
plt.ylabel("Square Numbers", fontsize=14)

# Assign range for each axis.
plt.axis([0, 302, 0, 27543608])

plt.show()