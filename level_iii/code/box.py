import matplotlib.pyplot as plt

data = [2, 9, 22, 34, 39, 42, 43, 46, 53, 55, 55, 63, 67, 72, 74, 74, 78, 79, 87, 95]

plt.boxplot(data)

plt.savefig('box.png')
