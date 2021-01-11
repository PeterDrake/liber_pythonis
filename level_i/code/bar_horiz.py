import matplotlib.pyplot as plt
flavors = ['chocolate', 'strawberry', 'tutti frutti', 'vanilla']
frequency = [6, 3, 2, 3]
plt.barh(flavors, frequency)
plt.ylabel('Ice Cream Flavors')
plt.xlabel('frequency')
plt.title('Favorite Ice Cream Flavors in Our Class')
plt.tight_layout()
plt.show()
