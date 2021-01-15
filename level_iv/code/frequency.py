import csv
import matplotlib.pyplot as plt

with open('nchs.csv') as file:
    reader = csv.DictReader(file)
    rows = [row for row in reader]

heights = [int(row['height']) for row in rows]

unique = list(set(heights))
counts = [heights.count(u) for u in unique]

plt.bar(unique, counts)

plt.ylabel('frequency')
plt.xlabel('height (inches)')
plt.title('Heights of children')

plt.tight_layout()
plt.savefig('frequency.png')
plt.show()
