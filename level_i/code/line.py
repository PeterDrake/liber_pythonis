import matplotlib.pyplot as plt

time = [12, 18, 24, 30, 36]
height = [25, 29, 36, 40, 43]

plt.plot(time, height)

plt.xlabel('time in months')
plt.ylabel('height in inches')
plt.title('Height of a Child Over Time')
plt.tight_layout()
plt.show()