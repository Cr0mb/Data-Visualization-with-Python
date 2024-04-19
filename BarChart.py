import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns            # Import Seaborn for stylish visualization
import numpy as np               # Import NumPy for numerical computations
import pandas as pd              # Import Pandas for data manipulation

# Sample data
x = ['A', 'B', 'C', 'D', 'E']  # Categories
y = [10, 20, 15, 25, 30]        # Values

# Create a figure and plot the data as bars
plt.figure(figsize=(8, 6))      # Set the figure size
plt.bar(x, y, color='skyblue')  # Plot bars with specified colors
plt.title('Bar Chart Example')   # Set the title of the plot
plt.xlabel('Categories')        # Set the label for the x-axis
plt.ylabel('Values')            # Set the label for the y-axis
plt.show()                      # Display the plot
