import pygal

from die import Die

# Creating a cube D6(3)
die_1 = Die()
die_2 = Die()
die_3 = Die()

# Simuation of a series of shots saving the results in the list.
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
max_result = die_1.num_sudes + die_2.num_sudes + die_3.num_sudes
for value in range(3, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visyalization of results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6, D6 and D6 1,000 times."
hist.x_labels = range(3, 19)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_cube3.svg')
