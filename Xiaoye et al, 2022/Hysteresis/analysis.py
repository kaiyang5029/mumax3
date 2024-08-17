import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the file
filename = 'table.txt'
data = pd.read_csv(filename, delim_whitespace=True, skiprows=2, header=None)

# Extract column 7 for x-axis and column 4 for y-axis
x = data[6]*1000
y = data[3]

# Plot the data
plt.figure(figsize=(8, 6))
plt.plot(x, y)
plt.xlabel('B_extz (mT)')
plt.ylabel('m_z ()')
plt.title('Fe0Co10_hysteresis')
plt.grid(True)
plt.savefig('Graph.png', dpi=300)
plt.show()
