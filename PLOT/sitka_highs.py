import csv
import matplotlib.pyplot as plt
from datetime import datetime

file_path = "PLOT/chapter_16/2261129.csv"

with open(file_path) as f:
  reader = csv.reader(f)
  reader_header = next(reader)

  avgs, dates = [], []
  for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
      avg = int(row[3])
    except ValueError:
      print(f"No value for {current_date}")
    else:
      avgs.append(avg)
      dates.append(current_date)


fig, ax = plt.subplots()
ax.plot(dates, avgs, c='blue')
plt.show()