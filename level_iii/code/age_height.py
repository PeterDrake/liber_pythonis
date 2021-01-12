import csv
import matplotlib.pyplot as plt

with open('data.csv') as file:
    reader = csv.DictReader(file)

rows = [row for row in reader]
ages = [int(row['age']) for row in rows]
heights = [int(row['height']) for row in rows]

plt.scatter(ages, heights)

plt.title('Age vs Height')
plt.xlabel('Age (months)')
plt.ylabel('Height (inches)')

plt.tight_layout()
# plt.show()

plt.savefig('../image/age_height.png')
