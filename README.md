# Mushroom Yield Forecasting

## Environment Setup

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```
### Activate Virtual Environment

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Smoke Test

```bash
python src/smoke_test.py
```

Expected Output:

```text
Sample Polyhouse Sensor Data:
   temperature  humidity  co2  yield_kg
0         24.5      88.2  950      12.4
```


## Task 4: Feature Engineering

### Objective

Prepared the dataset for machine learning by creating the feature matrix (X) and target variable (y), performing a chronological train-test split, and applying feature scaling without data leakage.

### Features and Target

**Features (X):**

* temperature
* humidity
* co2

**Target (y):**

* yield_kg

### Train-Test Split

A chronological 80/20 split was used to preserve the time-series nature of the dataset.

* Training Rows: 96
* Testing Rows: 24

**Train Period**

* Start: 2025-01-01 00:00:00
* End: 2025-01-04 23:00:00

**Test Period**

* Start: 2025-01-05 00:00:00
* End: 2025-01-05 23:00:00

### Feature Scaling

* MinMaxScaler was used for feature normalization.
* The scaler was fitted only on the training data.
* The test data was transformed using the fitted scaler.
* This approach prevents data leakage from the test set.

### Output Files

* data/processed/X_train.csv
* data/processed/X_test.csv
* data/processed/y_train.csv
* data/processed/y_test.csv
* models/scaler.joblib



## Task 5: Linear Regression Baseline

### Objective

Developed a baseline Linear Regression model to predict mushroom yield using environmental sensor measurements (temperature, humidity, and CO₂ concentration).

### Model Performance

| Metric   | Value |
| -------- | ----- |
| MAE      | 0.978 |
| RMSE     | 1.137 |
| R² Score | 0.01  |

The model was evaluated on the chronological test dataset. The results indicate that the model provides a basic predictive baseline but explains only a small proportion of the variation in mushroom yield.

### Coefficient Summary

| Feature     | Coefficient |
| ----------- | ----------: |
| Temperature |    0.087840 |
| Humidity    |   -0.214397 |
| CO₂         |   -0.127668 |

**Interpretation:**

* Temperature showed a positive relationship with mushroom yield.
* Humidity exhibited the strongest influence and showed a negative relationship with yield.
* CO₂ concentration also showed a negative association with yield in the observed dataset.
* Since the model was trained on scaled features, the coefficients represent relative influence rather than direct physical units.

### Diagnostic Conclusion

Residual analysis was performed using:

* Residuals vs Predicted Yield
* Residuals vs Humidity

The residuals were generally distributed around the zero line without severe systematic bias. However, the low R² score suggests that the linear model is unable to capture much of the variability in mushroom yield. This indicates that the relationship between environmental conditions and yield may be non-linear. Therefore, more advanced models such as Random Forest Regression should be explored and compared against this baseline model.

### Generated Artifacts

* `models/linear_regression.joblib`
* `reports/linear_metrics.json`
* `reports/linear_diagnostics.md`
* `reports/residuals_vs_predicted.png`
* `reports/residuals_vs_humidity.png`
