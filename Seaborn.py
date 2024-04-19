import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns            # Import Seaborn for stylish visualization
import numpy as np               # Import NumPy for numerical computations
import pandas as pd              # Import Pandas for data manipulation

# Sample data
np.random.seed(0)
data = np.random.randn(1000)  # Generate 1000 random numbers from a standard normal distribution

# Set Seaborn styling
sns.set(style='whitegrid')

# Create a figure and plot the data as a histogram with KDE
plt.figure(figsize=(8, 6))                # Set the figure size
sns.histplot(data, kde=True, color='salmon', bins=30)  # Plot histogram with kernel density estimate
plt.title('Histogram with KDE')           # Set the title of the plot
plt.xlabel('Values')                      # Set the label for the x-axis
plt.ylabel('Frequency')                   # Set the label for the y-axis
plt.show()                                # Display the plot
