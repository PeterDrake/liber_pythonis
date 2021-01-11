import matplotlib.pyplot as plt
flavors = ['chocolate', 'strawberry', 'tutti frutti', 'vanilla']
frequency = [6, 3, 2, 3] 
plt.bar(flavors, frequency)
plt.ylabel('frequency')
plt.xlabel('Ice Cream Flavors')
plt.title('Favorite Ice Cream Flavors in Our Class')
plt.tight_layout()
plt.show()
