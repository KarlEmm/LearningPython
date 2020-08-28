import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Explore the structure of the data.
filename = 'PLOT/MODIS_C6_Global_48h.csv'

with open(filename) as f:
  all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mag, lon, lat, hover_texts= [], [], [], []
for e in all_eq_dicts:
  if e['properties']['mag'] >= 4:
    mag.append(e['properties']['mag'])
    lon.append(e['geometry']['coordinates'][0])
    lat.append(e['geometry']['coordinates'][1])
    hover_texts.append(e['properties']['title'])


readable_file = './PLOT/readable_eq_data.json'
with open(readable_file, 'w') as f:
  json.dump(all_eq_data, f, indent=4)

# Map the earthquakes.
data = [{
  'type': 'scattergeo',
  'lon': lon,
  'lat': lat,
  'text': hover_texts,
  'marker': {
    'size': [5*m for m in mag],
    'color': mag,
    'colorscale': 'YlorBr',
    'colorbar': {'title': 'Magnitude'},
  },
}]
my_layout = Layout(title=f'{all_eq_data["metadata"]["title"]}')

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')