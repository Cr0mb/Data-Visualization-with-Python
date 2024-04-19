import matplotlib.pyplot as plt  # Import Matplotlib for basic plotting
import seaborn as sns            # Import Seaborn for stylish visualization
import numpy as np               # Import NumPy for numerical computations
import pandas as pd              # Import Pandas for data manipulation

# Sample data
x = np.linspace(0, 10, 100)  # Generate 100 evenly spaced numbers from 0 to 10
y = np.sin(x)                 # Compute sine of each number

# Create a figure and plot the data
plt.figure(figsize=(8, 6))    # Set the figure size
plt.plot(x, y, label='sin(x)')# Plot x versus y as lines and/or markers
plt.title('Sine Function')     # Set the title of the plot
plt.xlabel('x')                # Set the label for the x-axis
plt.ylabel('sin(x)')           # Set the label for the y-axis
plt.legend()                   # Display the legend
plt.grid(True)                 # Show grid lines
plt.show()  
