import csv_example
import matplotlib.pyplot as plt


def mean(ls):
    return sum(ls) / len(ls)


def average_price(year):
    with open('doxycycline_' + str(year) + '.csv') as file:
        reader = csv_example.DictReader(file)
        prices = [float(row['NADAC_Per_Unit']) for row in reader]
        return mean(prices)


def number_of_manufacturers(year):
    with open('doxycycline_' + str(year) + '.csv') as file:
        reader = csv_example.DictReader(file)
        labels = [row['NDC'] for row in reader]
        makers = [label[:4] for label in labels]  # The first four digits indicate the manufacturer
        return len(set(makers))


prices = [average_price(year) for year in range(2014, 2021)]
manufacturers = [number_of_manufacturers(year) for year in range(2014, 2021)]

plt.scatter(manufacturers, prices)
plt.xlabel('Number of manufacturers')
plt.ylabel('Average price')
plt.title('Doxycycline')
plt.show()
