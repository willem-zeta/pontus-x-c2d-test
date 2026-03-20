import pandas as pd
import numpy as np

# Read dataset from C2D input location
# In a C2D environment, the dataset is mounted at /data/inputs/
df = pd.read_csv("/data/inputs/did:op/0", header=0)

# Extract time and velocity columns
t = df["time_s"].values
v = df["velocity_ms"].values

# Fit gravitational acceleration g from v = g * t
# Using least squares: g = (t · v) / (t · t)
g_fitted = np.dot(t, v) / np.dot(t, t)

# Output results
print(f"Fitted gravitational acceleration: g = {g_fitted:.4f} m/s²")
print(f"Expected value:                    g = 9.8100 m/s²")
print(f"Difference:                            {abs(g_fitted - 9.81):.6f} m/s²")
