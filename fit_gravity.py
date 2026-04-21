import pandas as pd
import numpy as np
import glob
import os

# Read dataset from C2D input location (ocean-node v2 uses original filename)
files = [f for f in glob.glob('/data/inputs/**/*', recursive=True)
         if os.path.isfile(f) and not f.endswith('.json')]
df = pd.read_csv(files[0], header=0)

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


import os                                                                                                                                                                                                     
os.makedirs('/data/outputs', exist_ok=True)
with open('/data/outputs/result.txt', 'w') as f:                                                                                                                                                              
         f.write(f"Fitted gravitational acceleration: g = {g_fitted:.4f} m/s²\n")                                                                                                                                  
         f.write(f"Expected value:                    g = 9.8100 m/s²\n")
         f.write(f"Difference:                            {abs(g_fitted - 9.81):.6f} m/s²\n")                                                                                                                      
                                                                                                                                                                                                                
