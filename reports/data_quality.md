# Data Quality Report

## Dataset Overview

* Total Rows: 120
* Total Columns: 5
* Start Date: [Enter date from Step 6]
* End Date: [Enter date from Step 6]

## Data Quality Assessment

### Missing Values

| Column      | Missing Values |
| ----------- | -------------- |
| timestamp   | 0              |
| temperature | 0              |
| humidity    | 0              |
| co2         | 0              |
| yield_kg    | 0              |

Total Missing Values: **0**

### Duplicate Records

* Duplicate Rows Found: **0**

### Rule Violations

| Rule                       | Violations |
| -------------------------- | ---------- |
| Humidity between 0–100%    | 0          |
| Temperature between 0–50°C | 0          |
| CO₂ > 0 ppm                | 0          |
| Yield ≥ 0 kg               | 0          |

### Quality Score

* Rows Passing All Validation Rules: **100.00%**

---

## Descriptive Statistics

### Humidity (%)

* Mean: 78.64
* Median: 80.07
* Standard Deviation: 10.15

### Temperature (°C)

* Mean: 24.84
* Median: 24.85
* Standard Deviation: 1.85

### CO₂ (ppm)

* Mean: 989.66
* Median: 993.16
* Standard Deviation: 116.70

### Yield (kg)

* Mean: 13.09
* Median: 13.07
* Standard Deviation: 0.96

---

## Interpretation

### Humidity

The average humidity is 78.64%, with a median of 80.07%. Since the mean and median are close, humidity values are relatively balanced without significant skew. Humidity is slightly below the ideal mushroom cultivation range of 85–90%, suggesting room for environmental optimization.

### Temperature

The average temperature is 24.84°C with a standard deviation of 1.85°C. The low variation indicates stable temperature conditions throughout the monitoring period.

### CO₂ Concentration

The average CO₂ concentration is 989.66 ppm. The mean and median are nearly identical, indicating a consistent distribution with no major outliers.

### Yield

The average mushroom yield is 13.09 kg with a median of 13.07 kg. The small difference between mean and median suggests a symmetric yield distribution. The standard deviation of 0.96 kg indicates sufficient variability for predictive modeling while maintaining operational consistency.

### Overall Findings

1. The dataset contains 120 observations across 5 variables.
2. No missing values or duplicate records were found.
3. All records satisfy the defined validation rules.
4. Data quality is excellent, with a quality score of 100%.
5. Yield exhibits enough variation to support machine learning and forecasting tasks.

## Conclusion

The cleaned dataset is reliable and suitable for exploratory data analysis and predictive modeling. Environmental variables are stable, data quality is high, and no additional cleaning is required before visualization and model development.
