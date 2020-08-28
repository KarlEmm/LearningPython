import json

# Explore the structure of the data.
filename = 'PLOT/chapter_16/mapping_global_data_sets/data/eq_data_1_day_m1.json'

with open(filename) as f:
  all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']

mag, lon, lat = [], [], []
for e in all_eq_dicts:
  mag.append(e['properties']['mag'])
  lon.append(e['geometry']['coordinates'][0])
  lat.append(e['geometry']['coordinates'][1])


readable_file = './PLOT/readable_eq_data.json'
with open(readable_file, 'w') as f:
  json.dump(all_eq_data, f, indent=4)