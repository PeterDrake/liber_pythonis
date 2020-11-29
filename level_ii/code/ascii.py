import random

labels = ['water', 'earth', 'fire', 'air']
values = [9, 2, 5, 4]

# Find length of longest label
max_length = 0
for label in labels:
    if len(label) > max_length:
        max_length = len(label)

# Display plot
for i in range(len(labels)):
    padding = ' ' * (max_length - len(labels[i]))
    stars = '*' * values[i]
    print(padding + labels[i] + ': ' + stars)

