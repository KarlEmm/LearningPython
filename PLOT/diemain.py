from die import Die

die = Die()
result = []

for i in range(1000):
  result.append(die.roll())

frequencies = []
for v in range(1, die.num_sides + 1):
  frequencies.append(result.count(v))

print(frequencies)