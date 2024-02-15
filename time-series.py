import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Generate example time series data
np.random.seed(0)
date_range = pd.date_range(start='2024-02-01', end='2024-02-15', freq='H')
energy_consumption = np.random.randint(10, 50, len(date_range))

# Create DataFrame
df = pd.DataFrame({'timestamp': date_range, 'energy_consumption': energy_consumption})

# Plot energy consumption over time
plt.figure(figsize=(10, 6))
plt.plot(df['timestamp'], df['energy_consumption'], color='red', marker='o', linestyle='-')
plt.title('Energy Consumption Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Energy Consumption (kWh)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
