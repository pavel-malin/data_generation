import matplotlib.pyplot as plt

x_values = list(range(1, 6))
y_valuse = [x**3 for x in x_values]

plt.scatter(x_values, y_valuse, s=40)

# Assigning a chart title and axis labels.
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Numbers", fontsize=14)

# Assign range for each axis.
plt.axis([0, 50, 0, 150])

plt.show()