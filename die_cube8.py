import pygal

from die import Die

# Creating a cube D8.
die_1 = Die(8)
die_2 = Die(8)

# Simulation of a series of shots saving the results in the list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
max_result = die_1.num_sudes + die_2.num_sudes
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visyalization of results.
hist = pygal.Bar()

hist.title = "Results of rolling a D8 and a D8 1,000 times."
hist.x_labels = range(2, 17)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8 + D8', frequencies)
hist.render_to_file('die_cube8.svg')