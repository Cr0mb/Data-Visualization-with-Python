import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns            # Import Seaborn for stylish visualization
import numpy as np               # Import NumPy for numerical computations
import pandas as pd              # Import Pandas for data manipulation

# Sample data
np.random.seed(0)
x = np.random.randn(100)  # Generate 100 random numbers from a standard normal distribution
y = np.random.randn(100)  # Generate 100 random numbers from a standard normal distribution

# Create a figure and plot the data as scatter points
plt.figure(figsize=(8, 6))         # Set the figure size
plt.scatter(x, y, color='orange', alpha=0.6)  # Plot scatter points with specified color and transparency
plt.title('Scatter Plot Example')  # Set the title of the plot
plt.xlabel('X')                    # Set the label for the x-axis
plt.ylabel('Y')                    # Set the label for the y-axis
plt.show()                         # Display the plot
