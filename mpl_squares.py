import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(input_values, squares, linewidth=5)

# Assigning a chart title and axis labels.
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Numbers", fontsize=14)

# Assign font size for tick marks on axes.
plt.tick_params(axis='both', labelsize=14)

plt.show()
