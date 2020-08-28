from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

d1 = Die()
d2 = Die()
d3 = Die()
size = 1_000_000
results = []
#for n in range(size):
  #results.append(d1.roll() * d2.roll()) 
results = [(d1.roll() + d2.roll()) for x in range(size)]

frequencies = []
max_result = d1.num_sides + d2.num_sides 
min_result = 2 
frequencies = [results.count(s) for s in range(min_result, max_result +1)]
#for s in range(min_result, max_result + 1):
  #frequencies.append(results.count(s))

# Visualize the results.
x_values = list(range(min_result, max_result + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title=f'Results of rolling two D6 {size} times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')