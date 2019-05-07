import pygal

from die import Die

# Creating a cube d6.
die = Die()

# Simulation of a series of shots with saving the results in the list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
for values in range(1, die.num_sudes+1):
    frequency = results.count(values)
    frequencies.append(frequency)

# Visualization of results.
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')