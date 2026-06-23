# Mushroom Yield Forecasting System

## 1. Executive Summary

## 2. Problem Statement

## 3. Dataset Description

## 4. Data Cleaning

## 5. Exploratory Data Analysis

## 6. Modeling Approach

## 7. Model Evaluation

## 8. Deployment

## 9. Monitoring & Logging

## 10. Limitations

## 11. Future Improvements

## 12. Conclusion
 

 # Mushroom Yield Forecasting System

## 1. Executive Summary

This project presents an end-to-end machine learning solution for forecasting mushroom yield using environmental sensor data. The system predicts mushroom yield based on temperature, humidity, and CO₂ concentration measurements. The objective is to assist farmers and agritech stakeholders in making informed decisions by estimating expected yield under varying environmental conditions.

The project covers the complete machine learning lifecycle including data preprocessing, exploratory data analysis (EDA), model development, evaluation, deployment, monitoring, and cloud hosting. A Streamlit web application was developed and deployed to provide real-time predictions through an interactive user interface.

---

## 2. Problem Statement

Mushroom cultivation is highly dependent on environmental conditions. Variations in temperature, humidity, and CO₂ concentration can significantly affect productivity and crop quality.

The goal of this project is to develop a predictive analytics solution that estimates mushroom yield using sensor-based environmental data. Accurate yield forecasts can support production planning, resource optimization, and operational decision-making.

---

## 3. Dataset Description

The dataset contains environmental sensor readings collected from controlled mushroom farming conditions.

### Features

* Temperature (°C)
* Humidity (%)
* CO₂ Concentration (ppm)

### Target Variable

* Mushroom Yield (kg)

The dataset was prepared for supervised machine learning regression tasks where environmental variables are used to predict final yield.

---

## 4. Data Cleaning

Data preprocessing activities included:

* Missing value inspection
* Data type validation
* Duplicate record checking
* Outlier analysis
* Feature consistency verification

The cleaned dataset was used for exploratory analysis and model training.

---

## 5. Exploratory Data Analysis

EDA was conducted to understand relationships between environmental factors and mushroom yield.

### Key Findings

* Humidity showed a positive relationship with yield.
* Temperature demonstrated moderate influence on production.
* CO₂ levels contributed to yield variability.
* Yield values remained within expected operational ranges.

Visualization techniques included:

* Correlation analysis
* Distribution plots
* Feature relationship charts
* Actual vs Predicted comparisons

---

## 6. Modeling Approach

### Models Evaluated

1. Linear Regression
2. Random Forest Regressor

### Training Strategy

* Train-Test Split
* Cross Validation
* Hyperparameter Tuning using GridSearchCV

### Temporal Validation Rationale

Temporal validation helps simulate real-world deployment conditions by evaluating model performance on future observations rather than randomly sampled records. This approach reduces the risk of data leakage and provides a more realistic estimate of model performance.

---

## 7. Model Evaluation

### Evaluation Metric

Mean Absolute Error (MAE)

MAE represents the average absolute prediction error measured in kilograms.

### Champion Model

Random Forest Regressor

The Random Forest model achieved the best predictive performance and was selected as the production model.

### Results Summary

The selected model demonstrated reliable performance and improved predictive accuracy compared with baseline approaches.

---

## 8. Deployment

The trained model was integrated into a Streamlit web application.

### Application Features

* Real-time yield prediction
* Interactive sensor input controls
* Humidity sensitivity analysis
* Model information display
* Input validation warnings

### Deployment Platform

Streamlit Community Cloud

### Deliverables

* Public web application
* GitHub repository
* Model artifacts
* Monitoring documentation

---

## 9. Monitoring & Logging

A lightweight monitoring framework was implemented to track model usage.

### Logged Information

* Timestamp
* Temperature
* Humidity
* CO₂ concentration
* Predicted yield

### Monitoring Objectives

* Track prediction patterns
* Detect abnormal sensor inputs
* Monitor prediction drift
* Support future model retraining

### Retraining Triggers

* Significant increase in MAE
* Data distribution changes
* Sensor calibration updates
* Periodic model review

---

## 10. Limitations

Current limitations include:

* Limited dataset size
* Restricted environmental variables
* Absence of live IoT integration
* No automated retraining pipeline
* Limited production-scale validation

---

## 11. Future Improvements

Future enhancements may include:

1. Additional environmental sensors.
2. Real-time IoT integration.
3. Automated drift detection.
4. Scheduled model retraining.
5. Advanced ensemble models.
6. Historical trend dashboards.
7. Cloud-based monitoring services.

---

## 12. Conclusion

This project successfully demonstrates the complete machine learning workflow from data preparation and exploratory analysis to model deployment and monitoring. The Mushroom Yield Forecasting System provides real-time yield predictions through an interactive cloud-hosted application and serves as a practical example of machine learning applications in agritech and environmental forecasting.
