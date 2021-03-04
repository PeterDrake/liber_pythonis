import matplotlib.pyplot as plt

data1 = [2, 9, 22, 34, 39, 42, 43, 46, 53, 55, 55, 63, 67, 72, 74, 74, 78, 79, 87, 95]
data2 = [5, 5, 14, 14, 14, 31, 33, 47, 52, 63, 64, 65, 65, 69, 70, 76, 76, 77, 85, 89]

plt.boxplot([data1, data2], labels=['data1', 'data2'])

plt.savefig('two_boxes.png')
