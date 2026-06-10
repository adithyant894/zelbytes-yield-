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
