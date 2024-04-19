import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
data = np.random.randn(1000)

sns.set(style='whitegrid')

plt.figure(figsize=(8, 6))
sns.histplot(data, kde=True, color='salmon', bins=30)
plt.title('Histogram with KDE')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()