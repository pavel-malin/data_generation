import pygal

from die import Die

# Creating a cube D6 and D10.
die_1 = Die()
die_2 = Die(10)

# Simulation of a series of shots saving the results in the list.
results = []
for roll_num in range(5000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# Analysis of the results.
frequencies = []
max_result = die_1.num_sudes + die_2.num_sudes
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualization of results.
hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12',
                '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual0.svg')

