import matplotlib.pyplot as plt
data = [2, 3, 5, 1, 4]
plt.plot(data)
plt.title('Zombie outbreaks')
# plt.show()
plt.savefig('../image/simple_graph.png', bbox_inches='tight')
