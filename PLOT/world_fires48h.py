import csv

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Plots the world fires of the last 48h on a world map using Scattergeo from
# Plotly.

filename = 'PLOT/MODIS_C6_Global_48h.csv'
 # Prints the columns' header
with open(filename) as f:
  reader = csv.reader(f)
  column_header = next(reader)
  print(column_header)

  # Gathers geolocation data in two arrays
  lon, lat = [], []
  for row in reader:
    lat.append(row[0])
    lon.append(row[1])

data = [{
  'type': 'scattergeo',
  'lon': lon,
  'lat': lat,
  'marker': {
    'color': 'red',
    'colorscale': 'YlorBr',
  }
}]
my_layout = Layout(title='World Fires 2 Days')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='world_fires.html')





