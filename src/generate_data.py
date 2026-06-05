import pandas as pd
import numpy as np

np.random.seed(42)

n = 120

df = pd.DataFrame({
    "timestamp": pd.date_range("2025-01-01", periods=n, freq="h"),
    "temperature": np.random.normal(25, 2, n),
    "humidity": np.random.uniform(60, 95, n),
    "co2": np.random.uniform(800, 1200, n),
    "yield_kg": np.random.normal(13, 1, n)
})

df.to_csv("data/raw/polyhouse_sensors.csv", index=False)

print("Dataset created:", df.shape)
print("Saved to data/raw/polyhouse_sensors.csv")
