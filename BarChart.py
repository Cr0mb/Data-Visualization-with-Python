import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

x = ['A', 'B', 'C', 'D', 'E']
y = [10, 20, 15, 25, 30]

plt.figure(figsize=(8, 6))
plt.bar(x, y, color='skyblue')
plt.title('Bar Chart Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()