import pandas as pd

# Load dataset from ingestion step
df = pd.read_parquet("data/interim/01_loaded.parquet")

print("Loaded dataset successfully")
print("Shape:", df.shape)

# Step 1: Missing value audit
null_counts = df.isnull().sum()
null_percent = (df.isnull().mean() * 100).round(2)

print("\nMissing Values (Count):")
print(null_counts)

print("\nMissing Values (Percent):")
print(null_percent)

# Step 2: Duplicate timestamp check
duplicate_count = df.duplicated(subset=["timestamp"]).sum()

print("\nDuplicate Timestamps:", duplicate_count)

# Remove duplicates (keep first occurrence)
df = df.drop_duplicates(subset=["timestamp"], keep="first")

print("After removing duplicates:", df.shape)


# Step 3: Sensor validity rules

# Humidity must be between 0 and 100
invalid_humidity = df[(df["humidity"] < 0) | (df["humidity"] > 100)].shape[0]
df.loc[(df["humidity"] < 0) | (df["humidity"] > 100), "humidity"] = None

print("\nInvalid humidity rows corrected:", invalid_humidity)

# CO2 must be > 0
invalid_co2 = df[df["co2"] <= 0].shape[0]
df.loc[df["co2"] <= 0, "co2"] = None

print("Invalid CO2 rows corrected:", invalid_co2)

# Temperature sanity range (-10 to 50°C)
invalid_temp = df[(df["temperature"] < -10) | (df["temperature"] > 50)].shape[0]
df.loc[(df["temperature"] < -10) | (df["temperature"] > 50), "temperature"] = None

print("Invalid temperature rows corrected:", invalid_temp)
# Step 4: Imputation (after marking invalid values as NaN)

# Forward fill for sensor continuity
df["temperature"] = df["temperature"].ffill()
df["humidity"] = df["humidity"].ffill()
df["co2"] = df["co2"].ffill()

# If any NaNs still remain, fill with median
df["temperature"] = df["temperature"].fillna(df["temperature"].median())
df["humidity"] = df["humidity"].fillna(df["humidity"].median())
df["co2"] = df["co2"].fillna(df["co2"].median())

# IMPORTANT: Never impute target (yield_kg)
df = df.dropna(subset=["yield_kg"])

print("\nAfter Imputation - Missing Values:")
print(df.isnull().sum())

# Step 5: Save cleaned dataset
df.to_parquet("data/processed/02_cleaned.parquet", index=False)

print("\nCleaned dataset saved to data/processed/02_cleaned.parquet")
# Save cleaned CSV version
df.to_csv(
    "data/processed/02_cleaned.csv",
    index=False
)

print("Cleaned CSV saved.")