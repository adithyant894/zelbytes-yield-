# Task 2: Data Cleaning Log

## Dataset Overview
- Raw dataset loaded from polyhouse sensor logs
- Columns: timestamp, temperature, humidity, co2, yield_kg

---

## 1. Missing Value Analysis
- No missing values were found in the dataset
- Null handling was verified before transformation

---

## 2. Duplicate Handling
- Duplicate timestamps checked
- Result: 0 duplicates found
- Action: safe deduplication logic implemented for scalability

---

## 3. Sensor Validity Rules Applied

| Sensor | Rule | Action |
|--------|------|--------|
| Humidity | 0–100% | Invalid values set to NaN |
| CO₂ | > 0 | Invalid values set to NaN |
| Temperature | -10 to 50°C | Out-of-range values set to NaN |

---

## 4. Imputation Strategy

- Sensor columns:
  - Forward fill applied for temporal continuity
  - Median fallback for remaining missing values
- Target variable (`yield_kg`):
  - No imputation applied (to avoid label leakage)

---

## 5. Output Dataset
- Cleaned file saved as:
  `data/processed/02_cleaned.parquet`

---

## 6. Agritech Rationale

Polyhouse environments are continuous systems where:
- Temperature and humidity change gradually
- Sensor dropouts are temporary
- CO₂ spikes may indicate ventilation cycles

Hence:
- Temporal imputation (ffill) preserves sensor continuity
- Median fallback avoids skew from extreme values
- Target leakage is strictly avoided for model integrity
