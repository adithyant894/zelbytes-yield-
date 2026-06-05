import pandas as pd
from pathlib import Path

RAW_FILE = Path("data/raw/polyhouse_sensors.csv")
INTERIM_FILE = Path("data/interim/01_loaded.parquet")

df = pd.read_csv(
    RAW_FILE,
    parse_dates=["timestamp"]
)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 5 Rows:")
print(df.head())

print("\nInfo:")
df.info()
print("\nSummary Statistics:")
print(df.describe())

INTERIM_FILE.parent.mkdir(parents=True, exist_ok=True)
df.to_parquet(INTERIM_FILE, index=False)

print(f"\nSaved to {INTERIM_FILE}")






