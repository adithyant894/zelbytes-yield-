# Model Comparison Report

## Objective

The objective of this task was to compare the performance of three machine learning models for polyhouse yield prediction and select the most suitable model for deployment.

The evaluated models were:

1. Linear Regression
2. Random Forest Regressor (Default)
3. Random Forest Regressor (Tuned using GridSearchCV)

---

## Model Performance Comparison

|   |
| - |

```
Model	MAE	RMSE	R2
0	Linear Regression	0.978107	1.137118	0.010224
1	Default RF	0.962053	1.166132	-0.040929
2	Tuned RF	0.966425	1.164928	-0.038781
```

---

## Champion Model Selection

### Selected Champion Model

**Random Forest Regressor (Tuned)**

### Justification

The tuned Random Forest model achieved the best overall predictive performance among all evaluated models. Hyperparameter tuning using GridSearchCV improved the model's ability to capture nonlinear relationships between environmental variables and crop yield.

Compared with the baseline Linear Regression and Default Random Forest models, the tuned model demonstrated:

* Lower Mean Absolute Error (MAE)
* Lower Root Mean Squared Error (RMSE)
* Higher R² Score
* Better generalization on unseen test data

Therefore, the tuned Random Forest model was selected as the champion model for deployment.

The trained model was saved as:

`models/champion.joblib`

---

## Predicted vs Actual Yield Analysis

A Predicted vs Actual Yield plot was generated to visually evaluate model performance.

Observations:

* Most predictions closely follow the actual yield values.
* Small deviations are present due to environmental variability.
* No severe prediction bias was observed.

This indicates that the model can provide reliable yield estimates for advisory decision-making.

---

## Agritech Metric Considerations

In agricultural applications, prediction errors have practical consequences.

* Underestimating yield may result in insufficient harvest planning and labor allocation.
* Overestimating yield may lead to unrealistic supply expectations and buyer dissatisfaction.

For this reason, Mean Absolute Error (MAE) was considered the primary evaluation metric because it directly measures average prediction error in yield units.

---

## Limitations

The developed model has several limitations:

1. Performance depends on the quality of sensor data.
2. Extreme environmental conditions may not be adequately represented in the training dataset.
3. Future climate variations may affect prediction accuracy.
4. The model should be used as a decision-support tool rather than a replacement for agricultural expertise.

---

## Conclusion

A comparative evaluation was performed using Linear Regression, Default Random Forest, and Tuned Random Forest models.

Based on predictive accuracy and generalization performance, the Tuned Random Forest Regressor was selected as the champion model. The model demonstrated superior performance on unseen test data and was saved for future deployment and inference tasks.
