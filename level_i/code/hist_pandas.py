import matplotlib.pyplot as plt
import pandas as pd
data = pd.read_csv('kid_data_UsingR.csv')
plt.hist(data['height'], edgecolor='black',bins =4)
plt.ylabel('frequency')
plt.xlabel('heights in inches')
plt.title('Heights of Children')
plt.tight_layout()
plt.show()