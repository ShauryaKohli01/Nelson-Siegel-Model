# Importing Required Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.optimize import minimize

# Nelson-Siegel Function
def NelsonSiegel(b0, b1, b2, lb, t):
    A = (1 - np.exp(-t/lb)) / (t/lb)
    B = A - np.exp(-t/lb)
    return b0 + b1 * A + b2 * B
# Optimizer Function
def Optimizer(y, t):
    def Objective(x, actual, maturity):
        ns = NelsonSiegel(x[0], x[1], x[2], x[3], maturity)
        return np.sum((actual - ns)**2)
    x0 = [0.1, 0.1, 0.1, 0.1]
    res = minimize(Objective, x0, args=(y, t))
    return res.x

# Read Yield Data
dataset = pd.read_csv("C:/Users/dll/Downloads/trates.csv")[::-1]

#  Prepare Date and Maturity Columns
dates = dataset['Date'].values
del dataset['Date']
mats = dataset.columns.tolist()
dataset = dataset.values / 100.0

# Create Plotting Area
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(121, projection='3d')
ay = fig.add_subplot(122)

# Prepare Maturity Array
Y = dataset[-1]
T = np.array([1, 2, 3, 4, 6, 12, 24, 36, 60, 84, 120, 240, 360]) / 12.0
T = T[:len(Y)]  # in case your dataset has fewer maturities

# Optimize Parameters and Predict Yield Curve
b0, b1, b2, lb = Optimizer(Y, T)
YForecast = NelsonSiegel(b0, b1, b2, lb, T)

# 2D line plot
ay.plot(range(len(mats)), Y, color='red', label='Actual')
ay.plot(range(len(mats)), YForecast, color='blue', label='NS Fit')
ay.set_xticks(range(len(mats)))
ay.set_xticklabels(mats, rotation=45)
ay.legend()

# 3D surface plot
m, n = dataset.shape
x, y = np.meshgrid(range(m), range(n))
ax.plot_surface(x, y, dataset.T, cmap='jet')
ax.set_yticks(list(range(len(mats))))
ax.set_yticklabels(mats, rotation=35)

plt.tight_layout()
plt.show()