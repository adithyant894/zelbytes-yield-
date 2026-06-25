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



**Task 6**.

## Final CV Comparison

| Model             | Fold 1 MAE | Fold 2 MAE | Fold 3 MAE | Mean CV MAE |
| ----------------- | ---------- | ---------- | ---------- | ----------- |
| Linear Regression | 0.953      | 0.817      | 0.858      | 0.876       |
| Random Forest     | 0.904      | 0.858      | 0.806      | 0.856       |

### Interpretation

* Random Forest achieved a slightly lower Mean CV MAE (**0.856**) than Linear Regression (**0.876**).
* This indicates that Random Forest generalized slightly better across the time-based validation folds.
* However, the improvement was modest, suggesting that the dataset may not contain strong nonlinear relationships.

---

## Final Model Comparison

| Model             | MAE   | RMSE  | R²     |
| ----------------- | ----- | ----- | ------ |
| Linear Regression | 0.829 | 1.087 | -0.080 |
| Random Forest     | 0.962 | 1.166 | -0.041 |

### Discussion

* Linear Regression produced lower test MAE and RMSE.
* Random Forest produced a slightly better R² score.
* Cross-validation favored Random Forest, but the hold-out test set favored Linear Regression.
* Overall, neither model demonstrated strong predictive performance, indicating that additional feature engineering and hyperparameter tuning may be beneficial.

---

## Overfitting Discussion

### Training vs Testing Error

| Metric    | Value |
| --------- | ----- |
| Train MAE | 0.275 |
| Test MAE  | 0.962 |

### Interpretation

> The Random Forest model exhibited signs of overfitting. The training MAE (0.275) was substantially lower than the test MAE (0.962), indicating that the model fit the training data very closely but experienced reduced performance on unseen observations. This suggests limited generalization and highlights the need for hyperparameter optimization in future iterations.

---

## Task 7: Hyperparameter Tuning & Champion Model Selection

### Objective

The objective of this task was to optimize the Random Forest Regressor using GridSearchCV and compare its performance with the baseline Linear Regression and Default Random Forest models. The best-performing model was selected as the champion model for deployment.

### Methodology

1. Loaded the cleaned polyhouse yield dataset.
2. Selected the input features:

   * Temperature
   * Humidity
   * CO₂
3. Selected `yield_kg` as the target variable.
4. Performed a time-based train-test split to preserve chronological order.
5. Trained a baseline Linear Regression model.
6. Trained a Default Random Forest Regressor.
7. Applied GridSearchCV with TimeSeriesSplit cross-validation to tune:

   * `n_estimators`
   * `max_depth`
   * `min_samples_leaf`
8. Evaluated all models using:

   * Mean Absolute Error (MAE)
   * Root Mean Squared Error (RMSE)
   * R² Score
9. Compared model performance and selected a champion model.
10. Saved the champion model and best hyperparameters for future deployment.

### Hyperparameter Grid

```python
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [3, 5, 10],
    "min_samples_leaf": [1, 2, 4]
}
```

### Model Comparison

| Model                 | MAE   | RMSE  | R² Score |
| --------------------- | ----- | ----- | -------- |
| Linear Regression     | 0.978 | 1.137 | 0.010    |
| Default Random Forest | 0.962 | 1.166 | -0.041   |
| Tuned Random Forest   | 0.966 | 1.165 | -0.039   |

### Champion Model

The selected champion model was saved as:

```text
models/champion.joblib
```

The champion model was chosen based on overall predictive performance, model reliability, and suitability for deployment.

### Generated Artifacts

```text
models/
├── champion.joblib
└── rf_best_params.json

reports/
├── model_comparison.md
├── model_comparison.csv
├── gridsearch_results.csv
└── pred_vs_actual.png
```

### Key Learning Outcomes

* Implemented TimeSeriesSplit cross-validation.
* Performed hyperparameter tuning using GridSearchCV.
* Compared multiple regression models using evaluation metrics.
* Selected and serialized a deployment-ready champion model.
* Documented model performance and limitations for reproducibility.

# Task 8: Streamlit Yield Forecast Application

## Objective

Developed an interactive Streamlit application that loads the champion machine learning model and predicts mushroom yield from environmental sensor readings. The application provides a user-friendly interface for exploring how temperature, humidity, and CO₂ levels affect predicted yield.

## Features

### Interactive Inputs

The application allows users to adjust environmental conditions through sidebar controls:

* Temperature (°C)
* Humidity (%)
* CO₂ Concentration (ppm)

### Yield Prediction

* Loads the deployment-ready champion model (`champion.joblib`)
* Generates real-time mushroom yield predictions
* Displays results using Streamlit metric components
* Output expressed in kilograms (kg)

### Performance Optimization

* Implemented `@st.cache_resource`
* Prevents repeated model loading
* Improves application responsiveness

### Sensitivity Analysis

The application includes a humidity sensitivity chart that:

* Holds temperature and CO₂ constant
* Varies humidity across a predefined range
* Visualizes the predicted impact on mushroom yield

### Model Information

An expandable information panel displays:

* Model type
* Version information
* Input features
* Prediction target
* Evaluation summary

### Input Validation

User warnings are displayed when sensor values fall outside the recommended operating range, helping ensure responsible model usage.

---

## Application Workflow

1. Load the champion model.
2. Accept environmental sensor readings from the user.
3. Construct the feature dataframe.
4. Generate yield prediction.
5. Display predicted yield in kilograms.
6. Create humidity sensitivity analysis.
7. Present model metadata and validation messages.

---

## Run Instructions

### Launch Streamlit Application

```bash
streamlit run app.py
```

### Local Access

After launching, Streamlit provides a local URL similar to:

```text
http://localhost:8501
```

Open the URL in a web browser to access the application.

---

## Generated Artifacts

```text
app.py
models/champion.joblib
models/feature_columns.json
```

---

## Deliverables

* Working Streamlit application (`app.py`)
* Champion model integration
* Interactive prediction interface
* Sensitivity analysis visualization
* Application screenshot
* Updated README documentation

---

## Outcome

Successfully transformed the machine learning workflow into an interactive decision-support application capable of generating real-time mushroom yield forecasts from environmental sensor data. The application demonstrates deployment readiness and provides a foundation for future cloud deployment and stakeholder demonstrations.



Task 9 successfully deployed the Mushroom Yield Forecast application to Streamlit Community Cloud, making the solution publicly accessible through a live web URL. The deployment process included dependency management through a pinned requirements file, model artifact handling, application validation, and cloud hosting configuration.

Additionally, a lightweight monitoring framework was implemented through prediction logging, enabling the collection of input parameters and prediction outputs for future analysis. Monitoring documentation and retraining triggers were established to support model maintenance, performance tracking, and continuous improvement. This task completed the end-to-end machine learning lifecycle by transitioning the solution from local development to a production-ready cloud deployment environment.

Task 10: Technical Report & Capstone Presentation

Task 10 focused on documenting and presenting the complete Mushroom Yield Forecasting project. A comprehensive technical report was prepared covering the problem statement, dataset description, data cleaning, exploratory data analysis, model development, evaluation, deployment, monitoring, limitations, and future improvements. The final capstone presentation demonstrated the end-to-end machine learning workflow, including the deployed Streamlit application, model performance, monitoring strategy, and key project outcomes. This task showcased the successful completion of the project from data analysis to production deployment.
