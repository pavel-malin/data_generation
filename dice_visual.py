import pygal

from die import Die

# Creating a cube D6.
die_1 = Die()
die_2 = Die()

# Simulation of a series of shots with saving the results in the list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
max_result = die_1.num_sudes + die_2.num_sudes
for values in range(2, max_result+1):
    frequency = results.count(values)
    frequencies.append(frequency)

# Visualization of results.
hist = pygal.Bar()

hist.title = "Results of rolling two D6 dice 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6', frequencies)
hist.render_to_file('dice_visual.svg')