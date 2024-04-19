import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)

plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='orange', alpha=0.6)
plt.title('Scatter Plot Example')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()