import csv
from datetime import datetime

from matplotlib import pyplot as plt

# Get dates, high, and low temperatures from file.
filename = 'sitka_weather_2014.csv'
filename_0 = 'death_valley_2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

with open(filename_0) as g:
    reader_0 = csv.reader(g)
    header_row_0 = next(reader_0)
    
    dates_0, highs_0, lows_0 = [], [], []
    for row_0 in reader_0:
        try:
            current_date_0 = datetime.strptime(row_0[0], "%Y-%m-%d")
            high_0 = int(row_0[1])
            low_0 = int(row_0[3])
        except ValueError:
            print(current_date_0, 'missing data')
        else:
            dates_0.append(current_date_0)
            highs_0.append(high_0)
            lows_0.append(low_0)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(dates_0, highs_0, c='green', alpha=0.5)
plt.plot(dates_0, lows_0, c='black', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = "Daily high and low temperatures - 2014"
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
