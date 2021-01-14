import csv
import matplotlib.pyplot as plt

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]

unique = sorted(list(set(heights)))
counts = [heights.count(u) for u in unique]

plt.bar(unique, counts)

plt.ylabel('frequency')
plt.xlabel('height (inches)')
plt.title('Heights of children')
#plt.text(40, -5, 'Data: National Center for Health Statistics, "Dang, these kids are tall!"', horizontalalignment='center')
plt.tight_layout()
plt.show()
